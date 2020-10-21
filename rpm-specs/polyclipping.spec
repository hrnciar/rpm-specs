# The Clipper C++ crystallographic library already uses the name "clipper".
# The developer is fine with the choosen name.

# API monitoring
# http://upstream-tracker.org/versions/clipper.html

Name:           polyclipping
Version:        6.4.2
Release:        10%{?dist}
Summary:        Polygon clipping library

License:        Boost
URL:            http://sourceforge.net/projects/polyclipping
Source0:        http://downloads.sourceforge.net/%{name}/clipper_ver%{version}.zip

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qc

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in "Third Party/perl/perl_readme.txt" README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done


%build
pushd cpp
  %cmake
  %cmake_build
popd


%install
pushd cpp
  %cmake_install

# Install agg header with corrected include statement
  sed -e 's/\.\.\/clipper\.hpp/clipper.hpp/' < cpp_agg/agg_conv_clipper.h > %{buildroot}/%{_includedir}/%{name}/agg_conv_clipper.h
popd


%ldconfig_scriptlets


%files
%doc License.txt README
%doc "Third Party/Haskell" "Third Party/perl" "Third Party/ruby" "Third Party/python" Documentation
%{_libdir}/lib%{name}.so.*

%files devel
%{_datadir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Volker Fröhlich <volker27@gmx.at> - 6.4.2-6
- Resolve build failure
- Remove/correct manipulation bits (use_lines, perl README encoding)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 6.4.2-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Volker Fröhlich <volker27@gmx.at> - 6.4.2-1
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Miro Hrončok <mhroncok@redhat.com> - 6.4-1
- New upstream release (#1159525)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.2.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Oct 19 2014 Volker Fröhlich <volker27@gmx.at> - 6.2.0-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.3a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.3a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb  7 2014 Volker Fröhlich <volker27@gmx.at> - 6.1.3a-2
- Enable use_lines

* Fri Feb  7 2014 Volker Fröhlich <volker27@gmx.at> - 6.1.3a-1
- New upstream release

* Fri Jan 03 2014 Miro Hrončok <mhroncok@redhat.com> - 5.1.6-4
- Added patch to solve rounding error (#1047914)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Miro Hrončok <mhroncok@redhat.com> - 5.1.6-2
- Added patch to solve upstream bug 47

* Wed Jun  5 2013 Tom Hughes <tom@compton.nu> - 5.1.6-1
- Update to 5.1.6 upstream release
- Install agg_conv_clipper.h

* Fri Mar  1 2013 Volker Fröhlich <volker27@gmx.at> - 5.1.2-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Volker Fröhlich <volker27@gmx.at> - 5.0.3-1
- New upstream release

* Mon Jan  7 2013 Volker Fröhlich <volker27@gmx.at> - 5.0.2-1
- New upstream release
- Convert README to UTF8
- Add python directory as documentation

* Wed Dec 26 2012 Volker Fröhlich <volker27@gmx.at> - 4.10.0-1
- New upstream release

* Sat Dec  1 2012 Volker Fröhlich <volker27@gmx.at> - 4.9.7-1
- New upstream release

* Thu Nov 15 2012 Volker Fröhlich <volker27@gmx.at> - 4.9.6-1
- New upstream release

* Thu Sep 20 2012 Volker Fröhlich <volker27@gmx.at> - 4.8.8-1
- New upstream release

* Sat Jul 21 2012 Volker Fröhlich <volker27@gmx.at> - 4.8.5-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Volker Fröhlich <volker27@gmx.at> - 4.7.6-2
- Ship latest upstream sources and adapt to changes in build system
- Own subdirectory in includedir
- Keep timestamps with dos2unix

* Thu Apr 12 2012 Volker Fröhlich <volker27@gmx.at> - 4.7.6-1
- Initial package
