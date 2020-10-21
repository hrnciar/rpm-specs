%global packname repr
%global packver  1.1.0
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((leaflet)\\)

# Not available.
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Serializable Representations

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils, R-grDevices, R-htmltools, R-jsonlite, R-pillar >= 1.4.0, R-base64enc
# Suggests:  R-methods, R-highr, R-Cairo, R-stringr, R-testthat, R-diffobj >= 0.2.3, R-leaflet
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-grDevices
BuildRequires:    R-htmltools
BuildRequires:    R-jsonlite
BuildRequires:    R-pillar >= 1.4.0
BuildRequires:    R-base64enc
BuildRequires:    R-methods
BuildRequires:    R-highr
BuildRequires:    R-Cairo
BuildRequires:    R-stringr
BuildRequires:    R-testthat
BuildRequires:    R-diffobj >= 0.2.3
%if %{with_suggests}
BuildRequires:    R-leaflet
%endif

%description
String and binary representations of objects for several formats / mime types.


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
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Mon Apr 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Wed Feb 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.19.2-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15.0-1
- Update to latest version

* Sun Apr 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.0-2
- Remove extra Requires.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.0-1
- initial package for Fedora
