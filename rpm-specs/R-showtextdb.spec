%global packname showtextdb
%global packver  3.0
%global rlibdir  %{_datadir}/R/library

# Examples use the network.
%bcond_with network

Name:             R-%{packname}
Version:          3.0
Release:          2%{?dist}
Summary:          Font Files for the 'showtext' Package

License:          ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Load-existing-font-file.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-sysfonts >= 0.7, R-utils
# Suggests:  R-curl
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         wqy-microhei-fonts
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    wqy-microhei-fonts
BuildRequires:    R-sysfonts >= 0.7
BuildRequires:    R-utils
BuildRequires:    R-curl

%description
Providing font files that can be used by the 'showtext' package.


%prep
%setup -q -c -n %{packname}

# Remove bundled font references.
pushd %{packname}
rm inst/AUTHORS inst/COPYRIGHTS
%patch0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{rlibdir}/%{packname}
rm fonts/*
ln -s /usr/share/fonts/wqy-microhei/wqy-microhei.ttc fonts/wqy-microhei.ttc
popd


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-examples
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
%{rlibdir}/%{packname}/fonts


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.0-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-3
- Fix unbundling of fonts

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-1
- initial package for Fedora
