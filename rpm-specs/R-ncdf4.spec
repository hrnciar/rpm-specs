%global packname  ncdf4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.17
Release:          3%{?dist}
Summary:          Interface to Unidata netCDF (Version 4 or Earlier) Format Data Files

License:          GPLv3+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    netcdf-devel >= 4.1
BuildRequires:    chrpath

%description
Provides a high-level R interface to data files written using Unidata's netCDF
library (version 4 or earlier), which are binary data files that are portable
across platforms and include metadata information in addition to the data sets.
Using this package, netCDF files (either version 4 or "classic" version 3) can
be opened and data sets read in easily. It is also easy to create new netCDF
dimensions, variables, and files, in either version 3 or 4 format, and
manipulate existing netCDF files.


%prep
%setup -q -c -n %{packname}

# Remove license about bundled (but not on Fedora) HDF5.
rm %{packname}/inst/HDF5_COPYING


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Fix rpath.
chrpath -d %{buildroot}%{rlibdir}/%{packname}/libs/%{packname}.so


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.17-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17-1
- Update to latest version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.1-1
- Update to latest version

* Fri Mar 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16-2
- Remove library rpath

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16-1
- initial package for Fedora
