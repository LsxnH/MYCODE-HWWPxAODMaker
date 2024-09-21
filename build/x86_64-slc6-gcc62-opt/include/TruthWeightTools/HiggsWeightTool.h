/*
   Copyright (C) 2002-2018 CERN for the benefit of the ATLAS collaboration
 */

#pragma once

// EDM include(s):
#include "AsgTools/AnaToolHandle.h"
#include "PMGAnalysisInterfaces/IPMGTruthWeightTool.h"

// Local include(s):
#include "TruthWeightTools/HiggsWeights.h"
#include "TruthWeightTools/IHiggsWeightTool.h"

namespace TruthWeightTools
{

  /// Tool for accessing of MC weights and other weigthts for QCD uncertainty propagation for Higgs analyses
  ///
  /// @author Dag Gillberg <dag.gillberg@cern.ch>
  /// @author James Robinson <james.robinson@cern.ch>
  ///
  class HiggsWeightTool : public virtual IHiggsWeightTool, public asg::AsgTool
  {
    /// Create a proper constructor for Athena
    ASG_TOOL_CLASS(HiggsWeightTool, IHiggsWeightTool)

  public:

    /// Create a constructor for standalone usage
    HiggsWeightTool(const std::string &name);
    virtual ~HiggsWeightTool() {}

    virtual StatusCode initialize();

    virtual void printSummary();

    /// @name Function(s) accessed via the truth weight tool
    /// @{

    /// Get Higgs weights
    HiggsWeights getHiggsWeights(int HTXS_Njets30 = -1, double HTXS_pTH = -99.0, int HTXS_cat = -1);


    /// @}

  private:

    /// Get the MC weight vector
    const std::vector<float> getEventWeights() const;

    /// Value of MC event weight
    float getWeight(std::string weightName);

    /// Value of MC event weight
    bool hasWeight(std::string weightName);

    /// Index of MC event weight
    size_t getWeightIndex(std::string weightName);

    /// linear interpolation
    double linInter(double x, double x1, double y1, double x2, double y2);

    // returns hardcoded list of weight names matching expected weight structure
    std::vector<std::string> loadXMLWeightNames(const std::string& filename);

    /// Weight names in metadata
    const std::vector<std::string> getWeightNames();


    /// Access the HiggsWeights
    HiggsWeights getHiggsWeightsInternal(int HTXS_Njets30 = -1, double HTXS_pTH = -99.0, int HTXS_cat = -1);

    /// Protect against non-finite or outside-reqired-range weights
    void updateWeights(HiggsWeights &hw);
    void updateWeight(const double &w_nom, double &w);
    void updateWeights(const double &w_nom, std::vector<double> &ws) { for (auto &w : ws) updateWeight(w_nom, w); }
    void updateWeights(const double &w_nom, double &w1, double &w2) { updateWeight(w_nom, w1); updateWeight(w_nom, w2); }
    void updateWeights(const double &w_nom, double &w1, double &w2, double &w3) { updateWeights(w_nom, w1, w2); updateWeight(w_nom, w3); }


    /// Setup weights
    void setupWeights(size_t Nweights);

    /// getWeight
    double getWeight(size_t idx);
    double getWeight(const std::vector<float> &ws, size_t idx);

    size_t getIndex(std::string wn);

    /// Flags
    bool m_init;

    enum mode { AUTO = 0, FORCE_GGF_NNLOPS = 1, FORCE_POWPY8_VBF = 2, FORCE_POWPY8_VH = 3, FORCE_POWPY8_TTH = 4 };
    mode m_mode;
    bool m_forceNNLOPS, m_forceVBF, m_forceVH, m_forceTTH;

    /// number of expected weights
    size_t m_nWeights;

    /// Current MC channel number
    uint32_t m_mcID;

    /// The truth weight tool
    asg::AnaToolHandle<PMGTools::IPMGTruthWeightTool> m_weightTool;


    /// options
    bool m_requireFinite;
    bool m_cutOff;
    double m_weightCutOff;

    /// For statistics
    int m_Nnom, m_Nws;
    double m_sumw_nom, m_sumw2_nom, m_sumw, m_sumw2;
    double m_sumw_nomC, m_sumw2_nomC, m_sumwC, m_sumw2C;

    /// index of weights
    size_t m_nom;

    /// weight indices for PDF+alphaS uncertainites
    std::vector<size_t> m_pdfUnc, m_pdfNNPDF30;
    size_t m_aS_up, m_aS_dn;

    /// Special PDF sets
    size_t m_nnpdf30_nlo, m_nnpdf30_nnlo, m_mmht2014nlo, m_pdf4lhc_nlo, m_pdf4lhc_nnlo;
    size_t m_ct10nlo, m_ct10nlo_0118, m_ct14nlo, m_ct14nlo_0118;

    /// Special weight indices for Powheg NNLOPS
    size_t m_tinf, m_bminlo, m_nnlopsNom;
    std::vector<size_t> m_qcd, m_qcd_nnlops;

  };

} // namespace TruthWeightTools




// #pragma once

// // EDM include(s):
// #include "AsgTools/AnaToolHandle.h"
// #include "PMGAnalysisInterfaces/IPMGTruthWeightTool.h"
// #include "xAODTruth/TruthEvent.h"

// // Local include(s):
// #include "TruthWeightTools/IHiggsWeightTool.h"
// #include "TruthWeightTools/HiggsWeights.h"

// namespace TruthWeightTools
// {
//   /// Tool for accessing of MC weights and other weigthts for QCD uncertainty propagation for Higgs analyses
//   ///
//   /// @author Dag Gillberg <dag.gillberg@cern.ch>
//   ///
//   /// $Revision$
//   /// $Date$
//   ///
//   class HiggsWeightTool : public virtual IHiggsWeightTool, public asg::AsgTool
//   {

//     /// Create a proper constructor for Athena
//     ASG_TOOL_CLASS(HiggsWeightTool, TruthWeightTools::IHiggsWeightTool)

//   public:

//     /// Create a constructor for standalone usage
//     HiggsWeightTool(const std::string &name);

//     /// @name Function(s) implementing the asg::IAsgTool interface
//     /// @{

//     /// Function initialising the tool
//     virtual StatusCode initialize();

//     /// @}

//     // /// @name Function(s) implementing the IHiggsWeightTool interface
//     // /// @{

//     /// Implements interface from IHiggsWeightTool
//     HiggsWeights getHiggsWeights(int HTXS_Njets30 = -1, double HTXS_pTH = -99.0, int HTXS_cat = -1);

//     // Finalize method
//     virtual StatusCode finalize();

//   private:
//     void loadWeightNamesFromXML(const std::string& filename);

//     void setupWeightMapping();

//     float getMappedWeight(const std::string& group_name, const unsigned int& position = 0);

//     std::vector<std::string> m_weightNamesExpected;
//     // std::vector<std::string> m_weightNames;
//     std::map < std::string, std::vector<std::string> > m_weightNames;

//     // /// Implements interface from IHiggsWeightTool
//     // const std::vector<std::string>& getWeightNames() const;

//     // /// Implements interface from IHiggsWeightTool
//     // float getWeight(const std::string& weightName) const;

//     // /// Implements interface from IHiggsWeightTool
//     // bool hasWeight(const std::string& weightName) const;

//     // /// @}

// //     virtual ~HiggsWeightTool() {}


// // //     /// @name Function(s) accessed via the truth weight tool
// // //     /// @{

// //     /// Get the MC weight vector
// //     const std::vector<float> &getEventWeights() const;

// //     /// Value of MC event weight
// //     float getWeight(std::string weightName);

// //     /// Value of MC event weight
// //     bool hasWeight(const std::string &wName) const;

// //     // /// Index of MC event weight
// //     // size_t getWeightIndex(std::string weightName);
// //     size_t getWeightIndex(std::string weightName) { return 0; }



// //     // returns hardcoded list of weight names matching expecation
// //     // of ATLAS-default ggF NNLOPS
// //     const std::vector<std::string> getDefaultNNLOPSweightNames();
// //     const std::vector<std::string> getDefaultVBFweightNames();
// //     const std::vector<std::string> getDefaultVHweightNames();
// //     const std::vector<std::string> getDefaultTTHweightNames();

// //     /// Weight names in metadata
// //     const std::vector<std::string> &getWeightNames();

// // //     /// @}

// //   private:

// //     bool m_weightsAreCategorised;

// //     void categoriseWeightsByName();

// //     /// linear interpolation
// //     double linInter(double x, double x1, double y1, double x2, double y2);

// //     /// Access the HiggsWeights
// //     HiggsWeights getHiggsWeightsInternal(int HTXS_Njets30 = -1, double HTXS_pTH = -99.0, int HTXS_cat = -1);

// //     /// Protect against non-finite or outside-reqired-range weights
// //     void updateWeights(HiggsWeights &hw);
// //     void updateWeight(const double &w_nom, double &w);
// //     void updateWeights(const double &w_nom, std::vector<double> &ws) { for (auto &w : ws) updateWeight(w_nom, w); }
// //     void updateWeights(const double &w_nom, double &w1, double &w2) { updateWeight(w_nom, w1); updateWeight(w_nom, w2); }
// //     void updateWeights(const double &w_nom, double &w1, double &w2, double &w3) { updateWeights(w_nom, w1, w2); updateWeight(w_nom, w3); }


// //     /// Setup weights
// //     void setupWeights(size_t Nweights);

// // //     /// getWeight
// // //     double getWeight(size_t idx);
// //     double getWeight(const std::vector<float> &ws, size_t idx);
// //     // size_t getIndex(std::string wn);
// //     size_t getIndex(std::string wn) { return 0; }


// //     void loadDefaultWeightNames();

// //     /// Flags
// //     bool m_init;

// //     enum mode { AUTO = 0, FORCE_GGF_NNLOPS = 1, FORCE_POWPY8_VBF = 2, FORCE_POWPY8_VH = 3, FORCE_POWPY8_TTH = 4 };
// //     mode m_mode;
//     bool m_forceNNLOPS, m_forceVBF, m_forceVH, m_forceTTH;

// //     /// number of expected weights
// //     size_t m_nWeights;

// //     /// Current MC channel number
// //     uint32_t m_mcID;

// //     /// The truth weight tool
// //     // IPMGTruthWeightTool *m_weightTool;
//     asg::AnaToolHandle<PMGTools::IPMGTruthWeightTool> m_weightTool;

//     /// options
//     bool m_requireFinite;
//     bool m_cutOff;
//     double m_weightCutOff;

// //     /// For statistics
// //     int m_Nnom, m_Nws;
// //     double m_sumw_nom, m_sumw2_nom, m_sumw, m_sumw2;
// //     double m_sumw_nomC, m_sumw2_nomC, m_sumwC, m_sumw2C;

// //     /// index of weights
// //     size_t m_nom;
// //     // std::map <std::string, std::string> m_weightNames;

// //     /// weight indices for PDF+alphaS uncertainites
// //     std::vector<size_t> m_pdfUnc, m_pdfNNPDF30;
// //     size_t m_aS_up, m_aS_dn;

// //     /// Special PDF sets
// //     size_t m_nnpdf30_nlo, m_nnpdf30_nnlo, m_mmht2014nlo, m_pdf4lhc_nlo, m_pdf4lhc_nnlo;
// //     size_t m_ct10nlo, m_ct10nlo_0118, m_ct14nlo, m_ct14nlo_0118;

// //     /// Special weight indices for Powheg NNLOPS
// //     size_t m_tinf, m_bminlo, m_nnlopsNom;
// //     std::vector<size_t> m_qcd, m_qcd_nnlops;

// //   protected:
// //     /// EventInfo
// //     //const xAOD::EventInfo *m_evtInfo;
// //     //const xAOD::TruthEvent *m_truthEvt;
// //     //const std::vector<float> *m_weights;
//   };

// } // namespace xAOD
