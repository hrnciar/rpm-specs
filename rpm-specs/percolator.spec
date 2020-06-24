%undefine _ld_as_needed

Name:      percolator
Summary:   Software for postprocessing of shotgun proteomics data
Version:   3.05
Release:   2%{?dist}

## Code under src/ (except RAMP and Fido sub-directories) is licensed under a ASL 2.0 license.
## Code under src/Fido under MIT license.
## Code under src/MSToolkit under BSD license.
## Code under src/converters/MSToolkit/RAMP is licensed under a LGPLv2+ license.
License:   ASL 2.0 and MIT and BSD and LGPLv2+
URL:       https://github.com/percolator/percolator
Source0:   https://github.com/percolator/percolator/archive/rel-3-05/percolator-rel-3-05.tar.gz
## Example files for testing
## https://github.com/percolator/percolator/wiki/Example
Source1:   http://noble.gs.washington.edu/proj/percolator/data/yeast-01.sqt.tar.gz
Source2:   %{name}-RAMP_license_lgpl-2.1.txt

BuildRequires: gcc, gcc-c++
BuildRequires: cmake3

%if 0%{?el7}
BuildRequires: boost169-static, boost169-devel
BuildRequires: pkgconfig(tokyocabinet)
BuildRequires: pkgconfig(xerces-c)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: xsd, zlib-devel, bzip2-devel
%else
BuildRequires: boost-static, boost-devel
BuildRequires: pkgconfig(tokyocabinet)
BuildRequires: pkgconfig(xerces-c)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: xsd, zlib-devel, bzip2-devel
%endif

Requires: %{name}-data = %{version}-%{release}

%description
The first step in analyzing an mass spectrometry assay is to match
the harvested spectra against a target database 
using database search engines such as Sequest and Mascot,
a process that renders list of peptide-spectrum matches.
However, it is not trivial to assess the accuracy
of these identifications.

Percolator uses a semi-supervised machine learning to 
discriminate correct from incorrect peptide-spectrum matches,
and calculates accurate statistics such as q-value (FDR)
and posterior error probabilities.

%package data
Summary: percolator data files
BuildArch: noarch
Requires: xml-common

%description data
This package contains XSD data files of %{name} and
models of elude tool.

%package static
Summary: percolator static libraries

%description static
This package contains static libraries of %{name}.

%prep
%autosetup -n percolator-rel-3-05
tar -xvf %{SOURCE1}

## Remove spurious executable permissions
find . -type f -name "*.cpp" -exec chmod 0644 '{}' \;
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.xx" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec chmod 0644 '{}' \;

## Rename additional readme files
chmod a-x src/converters/MSToolkit/RAMP/README
mv src/converters/MSToolkit/RAMP/README src/converters/MSToolkit/RAMP/RAMP-README
mv src/converters/MSToolkit/RAMP/Readme.Mike.txt src/converters/MSToolkit/RAMP/RAMP-Readme.Mike.txt

## Included LGPLv2+ license
cp -p %{SOURCE2} RAMP_license_lgpl-2.1.txt

## Set 'qvality' destination directory
sed -e 's|./bin|bin|g' -i src/qvality/CMakeLists.txt

## Set 'elude models' destination directory
sed -e 's|${ELUDE_MODELS_PATH}..|${ELUDE_MODELS_PATH}|g' -i src/elude_tool/CMakeLists.txt
sed -e 's|${CMAKE_INSTALL_PREFIX}/share/elude/models/|${CMAKE_INSTALL_PREFIX}/share/elude|g' -i src/elude_tool/CMakeLists.txt

%build
mkdir -p percolator && pushd percolator
%cmake3 -Wno-dev \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE -DXML_SUPPORT:BOOL=ON \
%if 0%{?el7}
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/boost169" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags}" \
 -DBoost_FILESYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_filesystem.so \
 -DBoost_SERIALIZATION_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_serialization.so \
 -DBoost_SYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_system.so \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir}/boost169 \
 -DBoost_LIBRARY_DIR_RELEASE:PATH=%{_libdir}/boost169 \
 -DXML_SUPPORT:BOOL=OFF \
%else
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/tirpc" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
%endif
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DTARGET_ARCH=%{_arch} ..

### XSD files ran maually
### In Fedora 'xsd' executable is 'xsdcxx'
cd src
xsdcxx cxx-tree --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_in/13=percolatorInNs ../../src/xml/percolator_in.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_out/15=percolatorOutNs ../../src/xml/percolator_out.xsd
cd ..
###

%make_build
popd

mkdir -p fido && pushd fido
%cmake3 -Wno-dev \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DTokyoCabinet_INCLUDE_DIR=%{_includedir} \
 -DTokyoCabinet_LIBRARY=%{_libdir}/libtokyocabinet.so \
%if 0%{?el7}
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/boost169" \
 -DBoost_FILESYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_filesystem.so \
 -DBoost_SERIALIZATION_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_serialization.so \
 -DBoost_SYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_system.so \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir}/boost169 \
 -DBoost_LIBRARY_DIR:PATH=%{_libdir}/boost169 \
 -DBoost_LIBRARY_DIR_RELEASE:PATH=%{_libdir}/boost169 \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags}" \
 -DXML_SUPPORT:BOOL=OFF \
 %else
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/tirpc" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
%endif
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DTARGET_ARCH=%{_arch} ../src/fido
%make_build
popd

mkdir -p converters && pushd converters
%cmake3 -Wno-dev \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
%if 0%{?el7}
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/boost169" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags}" \
 -DBoost_FILESYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_filesystem.so \
 -DBoost_SERIALIZATION_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_serialization.so \
 -DBoost_SYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_system.so \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir}/boost169 \
 -DBoost_LIBRARY_DIR_RELEASE:PATH=%{_libdir}/boost169 \
 -DXML_SUPPORT:BOOL=OFF \
%else 
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/tirpc" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
%endif
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DPERCOLATOR-CONVERTERS_BINARY_DIR:STATIC=converters \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DTokyoCabinet_INCLUDE_DIR=%{_includedir} \
 -DTokyoCabinet_LIBRARY=%{_libdir}/libtokyocabinet.so \
 -DSERIALIZE="TokyoCabinet" \
 -DTARGET_ARCH=%{_arch} ../src/converters

### XSD files ran maually
### In Fedora 'xsd' executable is 'xsdcxx'
xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_in/13=percolatorInNs ../src/xml/percolator_in.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_out/15=percolatorOutNs ../src/xml/percolator_out.xsd
##
xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://psidev.info/psi/pi/mzIdentML/1.1=mzIdentML_ns ../src/xml/mzIdentML1.1.0.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://www.bioml.com/gaml/=gaml_tandem_ns ../src/xml/gaml_tandem1.0.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://www.thegpm.org/TANDEM/2011.12.01.1=tandem_ns --namespace-map =tandem_ns \
 --namespace-map http://www.bioml.com/gaml/=gaml_tandem_ns ../src/xml/tandem2011.12.01.1.xsd
###

%make_build
popd

mkdir -p elude && pushd elude
%cmake3 -Wno-dev \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DCMAKE_PREFIX_PATH:STRING=%{_prefix} \
 -DBoost_USE_STATIC_LIBS:BOOL=OFF \
 -DCMAKE_USE_RELATIVE_PATHS:BOOL=ON \
%if 0%{?el7}
 -DXML_SUPPORT:BOOL=OFF \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/boost169" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags}" \
 -DBoost_FILESYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_filesystem.so \
 -DBoost_SERIALIZATION_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_serialization.so \
 -DBoost_SYSTEM_LIBRARY_RELEASE:FILEPATH=%{_libdir}/boost169/libboost_system.so \
 -DBoost_INCLUDE_DIR:PATH=%{_includedir}/boost169 \
 -DBoost_LIBRARY_DIR_RELEASE:PATH=%{_libdir}/boost169 \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags}" \
%else
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -I../src -I%{_includedir}/tirpc" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
%endif
 -DTARGET_ARCH=%{_arch} ../src/elude_tool
%make_build
popd

%install
%make_install -C percolator
%make_install -C converters
%make_install -C elude

## Install static libraries
mkdir -p %{buildroot}%{_libdir}/percolator
for i in `find . -type f \( -name "*.a" \)`; do
 install -pm 755 $i %{buildroot}%{_libdir}/percolator
done

%check
mkdir -p test && cd test
../converters/sqt2pin -o pin.tab ../yeast-01.sqt ../yeast-01.shuffled.sqt
../percolator/src/percolator -X pout.xml pin.tab > yeast-01.psms

%files
# ASL 2.0 and MIT
%{_bindir}/percolator
# ASL 2.0 and LGPLv2+ and MIT and BSD
%{_bindir}/sqt2pin
%{_bindir}/qvality
%{_bindir}/elude
%{_bindir}/tandem2pin
%{_bindir}/msgf2pin

%files data
%doc ReadMe.txt
%doc src/converters/MSToolkit/RAMP/RAMP-*
%license license.txt
%license RAMP_license_lgpl-2.1.txt
%{_datadir}/elude/
%{_datadir}/percolator/
%{_datadir}/xml/percolator/

%files static
%doc ReadMe.txt
%doc src/converters/MSToolkit/RAMP/RAMP-*
%license license.txt
%license RAMP_license_lgpl-2.1.txt
%{_libdir}/percolator/

%changelog
* Tue May 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.05-2
- Fix EPEL7 builds (use boost169)

* Tue May 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.05-1
- Release 3.05
- Drop support for EPEL6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.04-1
- Release 3.04

* Thu Jul 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.03-1
- Release 3.03

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.02.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.02.01-1
- Release 3.02.01

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.02.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild 

* Thu Feb 22 2018 Antonio Trande <sagitterATfedoraproject.org> - 3.02.00-2
- Add gcc gcc-c++ BR

* Thu Feb 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.02.00-1
- Update to 3.02.0
- Drop old patches
- Link to libtirpc on fedora

* Sun Oct 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.01.02-1
- Update to 3.01.02

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.01-4
- URL changed to GitHub

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Jonathan Wakely <jwakely@redhat.com> - 3.01-2
- Rebuilt for Boost 1.63 and patched for GCC 7

* Thu Nov 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.01-1
- Update to 3.01

* Thu Jun 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.0-1
- Update to 3.0
- Use cmake3 on epel

* Sun Feb 07 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-11.20160205gita4d14b
- Fixed cflags to Boost148 (EPEL)

* Fri Feb 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-10.20160205gita4d14b
- Update to commit #a4d14b

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.10.1-8
- Rebuilt for Boost 1.60

* Wed Dec 23 2015 Antonio Trande <sagitter@fedoraproject.org> 2.10.1-7
- Used always 'cmake' command

* Sat Nov 14 2015 Antonio Trande <sagitter@fedoraproject.org> 2.10.1-6
- Fixed conditional OS macros for EPEL
- Set compiler/linker flags for hardened builds

* Thu Oct 01 2015 Antonio Trande <sagitter@fedoraproject.org> 2.10.1-5
- Boost directories modified to build in EPEL

* Sat Aug 08 2015 Antonio Trande <sagitter@fedoraproject.org> 2.10.1-4
- SPEC modified to build in EPEL
- Patch to replace all reference to xerces-c-3.1 in EPEL6

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sat Jul 18 2015 Antonio Trande <sagitter@fedoraproject.org> 2.10.1-2
- Rebuild for Boost upgrade to 1.58.0

* Tue Jul 07 2015 Antonio Trande <sagitter@fedoraproject.org> 2.10.1-1
- Update to 2.10.1
- Made a -static sub-package

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Antonio Trande <sagitter@fedoraproject.org> 2.09.0-4
- -data sub-package now requires xml-common

* Sun May 24 2015 Antonio Trande <sagitter@fedoraproject.org> 2.09.0-3
- The licensing breakdown is documented
- Removed spurious executable permissions
- /usr/share/xml is co-owned

* Sat May 23 2015 Antonio Trande <sagitter@fedoraproject.org> 2.09.0-2
- Added LGPLv2+ license of RAMP parser
- Made a data sub-package

* Fri May 22 2015 Antonio Trande <sagitter@fedoraproject.org> 2.09.0-1
- First package
