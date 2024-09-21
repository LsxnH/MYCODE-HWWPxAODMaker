/*
   Copyright (C) 2002-2018 CERN for the benefit of the ATLAS collaboration
 */

#pragma once

// // EDM include(s):
// #include "AsgTools/AsgMessaging.h"

// STL include(s):
#include <vector>

namespace TruthWeightTools
{
  /// Simple class for Higgs weights
  ///
  /// @author Dag Gillberg <dag.gillberg@cern.ch>
  ///
  class HiggsWeights
  {
  public:


    // HiggsWeights(const std::string& name) : asg::AsgMessaging(name) {}

    // virtual ~HiggsWeights() {}

    // // copy constructor
    // HiggsWeights(const HiggsWeights& other) : HiggsWeights(other.m_name) {}

    // // move constructor
    // HiggsWeights(HiggsWeights&& other) noexcept : cstring(std::exchange(other.cstring, nullptr)) {}

    // // copy assignment
    // HiggsWeights& operator=(const HiggsWeights& other)
    // {
    //      return *this = HiggsWeights(other);
    // }

    // // move assignment
    // HiggsWeights& operator=(HiggsWeights&& other) noexcept
    // {
    //     std::swap(cstring, other.cstring);
    //     return *this;
    // }



    // /// Constructor
    // // HiggsWeights();
    // HiggsWeights() : asg::AsgMessaging("HiggsWeights") {}

    // /// Destructor
    // virtual ~HiggsWeights() {};

    // // /// Copy constructor
    // // HiggsWeights();
    // // HiggsWeights(const HiggsWeights& other) : HiggsWeights(other.cstring)
    // // {}

    /// Nominal event weight
    double nominal, weight0;

    /// 30 PDF4LHC uncertainty variations + alphaS up/down
    std::vector<double> pdf4lhc_unc, nnpdf30_unc;
    double alphaS_up, alphaS_dn;

    /// Weights to reweigh central to a different PDF set
    /// If the PDF set is not present in file, this weight will be zero
    double nnpdf30_nlo, nnpdf30_nnlo, mmht2014nlo, pdf4lhc_nlo, pdf4lhc_nnlo;
    double ct10nlo, ct10nlo_0118, ct14nlo, ct14nlo_0118;

    /// QCD scale variations (muR,muF)
    std::vector<double> qcd;

    /// Special weights for Powheg ggF NNLOPS
    /// 1. QCD scale variations 3x(NNLO), 9xPowheg(muR,muF) - 26 variations
    std::vector<double> qcd_nnlops;

    /// 2. quark mass variations
    double mt_inf, mb_minlo;

    /// ggF specific uncertainty weights
    /// various different schemes

    /// WG1 proposed QCD uncertainty scheme
    double qcd_wg1_mu, qcd_wg1_res, qcd_wg1_mig01, qcd_wg1_mig12;
    double qcd_wg1_pTH, qcd_wg1_qm_b, qcd_wg1_qm_t, qcd_wg1_vbf2j, qcd_wg1_vbf3j;

    /// WG1 proposed uncertainty scheme
    std::vector<double> ggF_qcd_wg1();

    /// Tackmann proposed QCD uncertainty scheme
    std::vector<double> ggF_qcd_stxs;

    /// Merging of STXS and WG1 schemes
    std::vector<double> ggF_qcd_2017;

    /// Jet veto efficiency method for cross check
    std::vector<double> ggF_qcd_jve;

    /// Powheg NNLOPS possible scheme
    double qcd_nnlops_nnlo, qcd_nnlops_pow;

    /// information of the current event kinematiocs
    double pTH;
    int Njets30, STXS;

    /// methods to print weights to the screen
    char *uncStr(double var, double nom);

    void print();
  };

}