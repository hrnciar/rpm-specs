%global packname xml2
%global packver  1.3.2
%global rlibdir  %{_libdir}/R/library

%global with_suggests 0

Name:             R-%{packname}
Version:          1.3.2
Release:          2%{?dist}
Summary:          Parse XML

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-covr, R-curl, R-httr, R-knitr, R-magrittr, R-mockery, R-rmarkdown, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildRequires:    libxml2-devel
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-magrittr
BuildRequires:    R-mockery
BuildRequires:    R-testthat >= 2.1.0
%if %{with_suggests}
BuildRequires:    R-curl
BuildRequires:    R-httr
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%endif

%description
Work with XML files using a simple, consistent interface. Built on top of
the 'libxml2' C library.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


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
# Examples use the network.
%if %{with_suggests}
%{_bindir}/R CMD check %{packname} --no-examples
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-examples
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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.2-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.5-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-2
- Exclude Suggests for unavailable packages
- Fix tests against libxml2 2.9.10

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-9
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-7
- Fix broken test with new libxml2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-5
- Rewrite based on new template

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.0-4
- rebuild for R 3.5.0

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-3
- Add missing Rcpp Requires.
- Make library path explicit.

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-4
- Add missing Rcpp Requires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- New upstream release.

* Tue Nov 7 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-3
- Remove extra Suggests.

* Wed Nov 1 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-2
- Split include files into -devel package

* Mon Oct 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
