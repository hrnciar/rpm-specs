%global packname  ape
%global rlibdir  %{_libdir}/R/library

%bcond_with bootstrap

Name:             R-%{packname}
Version:          5.3
Release:          7%{?dist}
Summary:          Analyses of Phylogenetics and Evolution

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-nlme, R-lattice, R-graphics, R-methods, R-stats, R-tools, R-utils, R-parallel, R-Rcpp >= 0.12.0
# Suggests:  R-gee, R-expm, R-igraph
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-nlme
BuildRequires:    R-lattice
BuildRequires:    R-graphics
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-parallel
BuildRequires:    R-Rcpp-devel >= 0.12.0
%if %{without bootstrap}
BuildRequires:    R-gee
BuildRequires:    R-expm
BuildRequires:    R-igraph
%endif

%description
Functions for reading, writing, plotting, and manipulating phylogenetic
trees, analyses of comparative data in a phylogenetic framework, ancestral
character analyses, analyses of diversification and macroevolution,
computing distances from DNA sequences, reading and writing nucleotide
sequences as well as importing from BioConductor, and several tools such
as Mantel's test, generalized skyline plots, graphical exploration of
phylogenetic data (alex, trex, kronoviz), estimation of absolute
evolutionary rates and clock-like trees using mean path lengths and
penalized likelihood, dating trees with non-contemporaneous sequences,
translating DNA into AA sequences, and assessing sequence alignments.
Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
triangle methods, and several methods handling incomplete distance
matrices (NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some
functions call external applications (PhyML, Clustal, T-Coffee, Muscle)
whose results are returned into R.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 5.3-7
- rebuild for R 4
- turnoff bootstrap

* Sun Feb 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-6
- Add bootstrap setup to build without igraph

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 5.3-5
- rebuild against R without libRlapack.so

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.2-1
- Update to latest version
- Re-enable build checks
- Re-arrange to match latest template

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 5.1-1
- update to 5.1, rebuild for R 3.5.0

* Fri Mar 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.0-1
- initial package for Fedora
