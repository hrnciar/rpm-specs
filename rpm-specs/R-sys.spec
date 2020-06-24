%bcond_with check

%global packname  sys
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.3
Release:          3%{?dist}
Summary:          Powerful and Reliable Tools for Running System Commands in R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-unix >= 1.4, R-spelling, R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
%if %{with check}
BuildRequires:    R-unix >= 1.4
BuildRequires:    R-spelling
BuildRequires:    R-testthat
%endif

%description
Drop-in replacements for the base system2() function with fine control and
consistent behavior across platforms. Supports clean interruption, timeout,
background tasks, and streaming STDIN / STDOUT / STDERR over binary or text
connections. Arguments on Windows automatically get encoded and quoted to work
on different locales.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# A file used in tests; tests aren't installed.
rm %{buildroot}%{rlibdir}/%{packname}/utf8.txt


%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 3.3-3
- conditionalize check to break loop
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-1
- initial package for Fedora
