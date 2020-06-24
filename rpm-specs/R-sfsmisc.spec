%global packname sfsmisc
%global packver  1.1-7
%global rlibdir  %{_datadir}/R/library

# lokern requires this package.
%global with_loop 0

Name:             R-%{packname}
Version:          1.1.7
Release:          2%{?dist}
Summary:          Utilities from 'Seminar fuer Statistik' ETH Zurich

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices, R-methods, R-utils, R-stats
# Suggests:  R-datasets, R-tcltk, R-cluster, R-lattice, R-MASS, R-Matrix, R-nlme, R-lokern
# LinkingTo:
# Enhances:

BuildArch:        noarch
Suggests:         procps-ng
BuildRequires:    procps-ng
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grDevices
BuildRequires:    R-methods
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-datasets
BuildRequires:    R-tcltk
BuildRequires:    R-cluster
BuildRequires:    R-lattice
BuildRequires:    R-MASS
BuildRequires:    R-Matrix
BuildRequires:    R-nlme
%if %{with_loop}
BuildRequires:    R-lokern
%endif

%description
Useful utilities ['goodies'] from Seminar fuer Statistik ETH Zurich, some of
which were ported from S-plus in the 1990's. For graphics, have pretty
(Log-scale) axes, an enhanced Tukey-Anscombe plot, combining histogram and
boxplot, 2d-residual plots, a 'tachoPlot()', pretty arrows, etc. For
robustness, have a robust F test and robust range(). For system support,
notably on Linux, provides 'Sys.*()' functions with more access to system and
CPU information. Finally, miscellaneous utilities such as simple efficient
prime numbers, integer codes, Duplicated(), toLatex.numeric() and is.whole().


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{with_loop}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.7-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.7-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.5-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.2-1
- initial package for Fedora
