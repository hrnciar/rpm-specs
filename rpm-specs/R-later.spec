%global packname  later
%global rlibdir  %{_libdir}/R/library

# rmarkdown is not yet available.
%global with_doc 1

Name:             R-%{packname}
Version:          1.1.0.1
Release:          1%{?dist}
Summary:          Utilities for Scheduling Functions to Execute Later with Event Loops

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
# Remove bundled tinycthread and use C11 threads directly.
Source1:          tinycthread-threads-wrapper.h

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.9, R-rlang
# Suggests:  R-knitr, R-rmarkdown, R-testthat
# LinkingTo: R-Rcpp, R-BH
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.9
BuildRequires:    R-BH-devel
BuildRequires:    R-rlang
BuildRequires:    R-testthat
%if %{with_doc}
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%endif

%description
Executes arbitrary R or C functions some time after the current time, after the
R execution stack has emptied. The functions are scheduled in an event loop.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

# Ensure we don't use this bundled code.
rm %{packname}/src/{badthreads.h,tinycthread.c}
cp %SOURCE1 %{packname}/src/tinycthread.h
sed -i -e '/badthread/d' -e '/tinycthread/d' %{packname}/MD5


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# A file used in tests; tests aren't installed.
rm %{buildroot}%{rlibdir}/%{packname}/bgtest.cpp


%check
%if %{with_doc}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0.1-1
- update to 1.1.0.1
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.5-1
- Update to latest version

* Tue Sep 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.4-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.3-1
- Update to latest version
- Enable documentation

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.7.2-2
- rebuild for R 3.5.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- Update to latest version

* Fri Apr 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.1-2
- Remove unnecessary Requires

* Fri Apr 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.1-1
- initial package for Fedora
