Name:           petpvc
Version:        1.2.4
Release:        7%{?dist}
Summary:        Tools for partial volume correction (PVC) in positron emission tomography (PET) 

License:        ASL 2.0
URL:            https://github.com/UCL/PETPVC
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(ITK)
# XXX: this is workaround for bug in ITK
# /usr/include/InsightToolkit/itkNumericTraits.h:45:10: fatal error: vcl_limits.h: No such file or directory
#  #include "vcl_limits.h" // for std::numeric_limits
#           ^~~~~~~~~~~~~~
BuildRequires:  vxl-devel
# XXX: this is workaround for bug in ITK
BuildRequires:  gdcm-devel
# make[2]: *** No rule to make target '/usr/lib64/libfftw3.so', needed by 'src/pvc_vc'.  Stop.
BuildRequires:  fftw-devel
BuildRequires:  gtest-devel
BuildRequires:  libminc-devel
# make[2]: *** No rule to make target '/usr/lib64/libXext.so', needed by 'src/pvc_relabel'.  Stop.
# (and quite a few more of these)
BuildRequires: libXext-devel

%description
%{summary}.

%prep
%autosetup -n PETPVC-%{version}
# Do not install examples
sed -i -e "/parc/d" CMakeLists.txt

%build
flags=( -std=gnu++11
        -Wno-unused-variable
        -Wno-unused-but-set-variable
        -Wno-unused-local-typedefs
      )

export ITK_DIR=%{_libdir}/cmake/InsightToolkit
%cmake \
-DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS ${flags[*]}"
# no idea where -lGTest::GTest comes from. It doesn't seem to work.
grep -r GTest::Main -l|xargs sed -r -i 's/GTest::Main/gtest_main/; s/GTest::GTest/gtest/'

%cmake_build

%install
%cmake_install

%check
# Let it run serial
%global _smp_mflags "-j1"
%ctest

%files
%license LICENSE.txt
%doc README.md parc
%{_bindir}/petpvc
%{_bindir}/pvc_*

%changelog
* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-7
- Use correct cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-4
- Add missing BR to fix FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-1
- Update to latest version, fix build.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-3
- Rebuild for VTK 8.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.9.git8b28893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.8.git8b28893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.7.git8b28893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 7 2016 Orion Poplawski <orion@cora.nwra.com> - 0.0.0-0.6.git8b28893
- Rebuild for vtk 7.1

* Sat Jul 02 2016 Orion Poplawski <orion@cora.nwra.com> - 0.0.0-0.5.git8b28893
- Rebuild for hdf5 1.8.17

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.0-0.4.git8b28893
- Build with gnu++98 until dependencies support c++11 (fix FTBFS)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.3.git8b28893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Orion Poplawski <orion@cora.nwra.com> - 0.0.0-0.2.git8b28893
- Rebuild for hdf5 1.8.16

* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git8b28893
- Update with new upstream repo
- Fix things according review

* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git775857a
- Initial package
