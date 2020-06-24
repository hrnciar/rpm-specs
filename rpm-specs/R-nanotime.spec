%global packname  nanotime
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((xts)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          0.2.4
Release:          5%{?dist}
Summary:          Nanosecond-Resolution Time for R

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods, R-bit64, R-RcppCCTZ >= 0.2.3, R-zoo
# Suggests:  R-RUnit, R-data.table, R-xts
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-bit64
BuildRequires:    R-RcppCCTZ >= 0.2.3
BuildRequires:    R-zoo
BuildRequires:    R-RUnit
BuildRequires:    R-data.table
%if %{with_suggests}
BuildRequires:    R-xts
%endif

%description
Full 64-bit resolution date and time support with resolution up to
nanosecond granularity is provided, with easy transition to and from the
standard 'POSIXct' type.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/unitTests


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.2.4-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version

* Fri Jul 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- initial package for Fedora
