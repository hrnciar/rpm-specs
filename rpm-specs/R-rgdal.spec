%global packname  rgdal
%global packver   1.5
%global packrel   8
%global rlibdir  %{_libdir}/R/library
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          1%{?dist}
Summary:          Bindings for the 'Geospatial' Data Abstraction Library

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-sp >= 1.1-0
# Imports:   R-grDevices, R-graphics, R-stats, R-utils
# Suggests:  R-knitr, R-RSQLite, R-maptools, R-mapview
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-sp-devel >= 1.1.0
BuildRequires:    R-grDevices
BuildRequires:    R-graphics
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    gdal-devel >= 1.11.4
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel
%if %{with_suggests}
BuildRequires:    R-knitr
BuildRequires:    R-RSQLite
BuildRequires:    R-maptools
BuildRequires:    R-mapview
%endif

%description
Provides bindings to the 'Geospatial' Data Abstraction Library ('GDAL') and
access to projection/transformation operations from the 'PROJ.4' library. Both
'GDAL' raster and 'OGR' vector map data can be imported into R, and 'GDAL'
raster data and 'OGR' vector data exported. Use is made of classes defined in
the 'sp' package.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Bundled projects.h from proj; not needed.
rm inst/include/projects.h
rmdir inst/include
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Remove unnecessary documentation.
rm %{buildroot}%{rlibdir}/%{packname}/README.windows
rm %{buildroot}%{rlibdir}/%{packname}/SVN_VERSION
# Remove unnecessary autoconf macros.
rm -r %{buildroot}%{rlibdir}/%{packname}/m4


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/README
%license %{rlibdir}/%{packname}/LICENSE.TXT
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/OSGeo4W_test
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/pictures
%{rlibdir}/%{packname}/vectors


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.8-1
- update to 1.5-8
- rebuild for R 4

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.4.8-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.4.8-3
- Rebuild (gdal)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.8-1
- Update to latest version

* Mon Oct 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-1
- Update to latest version

* Wed Oct 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-1
- Update to latest version

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-4
- Remove old proj subpackage dependencies

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- Update to latest version

* Thu Mar 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.9-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.6-1
- Update to latest version

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-3
- Rebuilt for updated Proj

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.3-1
- Update to latest version

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.20-2
- rebuild for R 3.5.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.20-1
- Update to latest version

* Tue Mar 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.18-1
- initial package for Fedora
