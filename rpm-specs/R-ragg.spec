%global packname ragg
%global packver  0.3.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Graphic Devices Based on AGG

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# https://github.com/r-lib/ragg/pull/49
Patch0001:        0001-Byte-swap-agg_capture-output-on-big-endian-systems.patch
Patch0002:        0002-Use-WORDS_BIGENDIAN-from-Rconfig.h.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-systemfonts >= 0.2.1
# Suggests:  R-covr, R-testthat, R-grid, R-graphics
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-systemfonts-devel >= 0.2.1
BuildRequires:    R-testthat
BuildRequires:    R-grid
BuildRequires:    R-graphics

BuildRequires:    gcc-c++
BuildRequires:    pkgconfig(freetype2)
BuildRequires:    pkgconfig(libpng)
BuildRequires:    pkgconfig(libtiff-4)
BuildRequires:    libjpeg-devel

%description
Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D drawing
library. The 'ragg' package provides a set of graphic devices based on AGG to
use as alternative to the raster devices provided through the 'grDevices'
package.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
%patch0002 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname} || (cat %{packname}.Rcheck/tests/testthat.Rout.fail && exit 1)


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-2
- Rebuild to fix dist tag

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- initial package for Fedora
