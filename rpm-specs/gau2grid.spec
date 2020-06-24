Name:           gau2grid
Version:        1.3.1
Release:        2%{?dist}
Summary:        Fast computation of a gaussian function and its derivative on a grid
License:        BSD
URL:            https://github.com/dgasmith/gau2grid
Source0:        https://github.com/dgasmith/gau2grid/archive/v%{version}/%{name}-%{version}.tar.gz

# Try to find Python3 from the start
Patch0:         gau2grid-1.3.1-py3.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-numpy

%description
A collocation code for computing gaussians on a grid of the form:
out_Lp = x^l y^m z^n \sum_i coeff_i e^(exponent_i * (|center - p|)^2)

This version has been built with -DCARTESIAN_ORDER=row
-DSPHERICAL_ORDER=gaussian for compatibility with psi4.

%package devel
Summary:        Development headers for gau2grid
Requires:       cmake
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for gau2grid.

%prep
%autosetup

%build
mkdir objdir
cd objdir
%cmake .. -DCARTESIAN_ORDER=row -DSPHERICAL_ORDER=gaussian -DCMAKE_INSTALL_LIBDIR=%{_lib}
%{make_build}
cd ..

%install
%{make_install} -C objdir

%files
%license LICENSE
%doc README.md
%{_libdir}/libgg.so.1*

%files devel
%{_includedir}/gau2grid/ 
%{_datadir}/cmake/gau2grid/
%{_libdir}/libgg.so

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5.25cf057git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.25cf057git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-3.25cf057git
- Update to 25cf057git to address FTBFS issues.

* Sun Sep 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-2
- Review fixes, including addition of soname.

* Sat Sep 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-1
- Initial release.
