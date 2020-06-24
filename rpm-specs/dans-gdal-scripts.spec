Name:           dans-gdal-scripts
Version:        0.24
Release:        11%{?dist}
Summary:        Utilities for use in conjunction with GDAL

License:        BSD
URL:            https://github.com/gina-alaska/dans-gdal-scripts
Source0:        https://github.com/gina-alaska/dans-gdal-scripts/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gdal-devel
BuildRequires:  proj-devel

# Tests are using
BuildRequires:  netpbm-progs

%description
Dan Stahlke's GDAL contributed tools are a collection of
useful programs to perform common raster operations.


%prep
%setup -q 
./autogen.sh
%configure


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%check
pushd src/tests
./test1.sh
./test2.sh
./test3.sh
# TIFFReadDirectory warnings are harmless, according to the author


%files
%doc LICENSE README.md ChangeLog TODO
%{_bindir}/gdal_*


%changelog
* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 0.24-11
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 0.24-10
- Rebuild (gdal)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Volker Froehlich <volker27@gmx.at> - 0.24-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.23-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sun Jul 26 2015 Volker Froehlich <volker27@gmx.at> - 0.23-10
- Rebuild for GDAL 2.0

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.23-9
- rebuild for Boost 1.58

* Mon Jul 06 2015 Volker Fröhlich <volker27@gmx.at> - 0.23-8
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.23-6
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.23-3
- Rebuild for boost 1.55.0

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 0.23-2
- Rebuild for gdal 1.10.0

* Sat Aug 03 2013 Volker Fröhlich <volker27@gmx.at> - 0.23-1
- New upstream release
- Remove -Werr patch (solved)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-0.4.20130522git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.21-0.3.20130522git
- Rebuild for boost 1.54.0

* Mon Jun 10 2013 Volker Fröhlich <volker27@gmx.at> - 0.21-0.2.20130522git
- Make the werror patch apply

* Tue May 21 2013 Volker Fröhlich <volker27@gmx.at> - 0.21-0.1.20130522git
- Initial package for Fedora
