%global packname svglite
%global packver  1.2.3
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((fontquiver)\\)

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          An 'SVG' Graphics Device

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp, R-gdtools >= 0.1.6
# Suggests:  R-htmltools, R-testthat, R-xml2 >= 1.0.0, R-covr, R-fontquiver >= 0.2.0, R-knitr, R-rmarkdown
# LinkingTo: R-Rcpp, R-gdtools, R-BH
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-gdtools-devel >= 0.1.6
BuildRequires:    R-BH-devel
BuildRequires:    R-htmltools
BuildRequires:    R-testthat
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%if %{with_suggests}
BuildRequires:    R-fontquiver >= 0.2.0
%endif

%description
A graphics device for R that produces 'Scalable Vector Graphics'. 'svglite'
is a fork of the older 'RSvgDevice' package.


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
export LANG=C.UTF-8
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-tests
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


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.3-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Update to latest version

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- initial package for Fedora
