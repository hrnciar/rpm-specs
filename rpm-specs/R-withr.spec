%bcond_without bootstrap

%global packname withr
%global packver  2.3.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.3.0
Release:          1%{?dist}
Summary:          Run Code 'With' Temporarily Modified Global State

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-grDevices, R-stats
# Suggests:  R-covr, R-DBI, R-knitr, R-lattice, R-methods, R-rmarkdown, R-RSQLite, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-stats
%if %{without bootstrap}
BuildRequires:    R-DBI
BuildRequires:    R-knitr
BuildRequires:    R-lattice
BuildRequires:    R-methods
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite
BuildRequires:    R-testthat >= 2.1.0
%endif

%description
A set of functions to run code 'with' safely and temporarily modified
global state. Many of these functions were originally a part of the
'devtools' package, this provides a simple package with limited
dependencies to provide access to these functions.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
export LANG=C.UTF-8
%if %{with_doc}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
%endif
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Wed Sep 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version (#1881624)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.0-2
- conditionalize check to break testthat loop
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.2-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.2-1
- Update to latest version.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.1-1
- Update to latest release.

* Wed Nov 15 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.0-2
- Remove lattice from Requires.
- Minor fixes to spec internals.

* Fri Nov 10 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.0-1
- Update to latest release.

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.0.0-3
- Remove extra Requires.

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.0.0-2
- Clean up old stuff in spec.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.0.0-1
- Update to latest release.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.0.0-1
- New upstream release

* Fri Feb 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.2-1
- initial package for Fedora
