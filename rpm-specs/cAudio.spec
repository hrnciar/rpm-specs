# This is the upstream-preferred name of the project
Name:           cAudio
Version:        2.3.1
Release:        13%{?dist}
Summary:        3D Audio Engine Based on Openal

License:        zlib
URL:            https://github.com/R4stl1n/cAudio/
Source0:        https://github.com/R4stl1n/cAudio/archive/%{version}/cAudio-%{version}.tar.gz

# Patch to version the .so names of the plugins.
# Was submitted upstream and merged (see https://github.com/R4stl1n/cAudio/pull/45)
Patch0:         https://patch-diff.githubusercontent.com/raw/R4stl1n/cAudio/pull/45.patch

# We need cmake and a compiler, obviously.
BuildRequires:  gcc-c++, cmake

BuildRequires:  libogg-devel, libvorbis-devel, openal-soft-devel

BuildRequires:  doxygen, graphviz

# Obsolete and provide cAudio-freeworld.
Obsoletes:      cAudio-freeworld < 2.3.1-4
Provides:       cAudio-freeworld = %{version}-%{release}

%description
cAudio is a 3D audio engine based on OpenAL.

# this subpackage maybe should be merged into -devel or -doc

%package examples

Summary:       Examples for cAudio
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description examples

A set of examples for cAudio.

%package devel

Summary:       Development headers for cAudio
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel

Development files and library headers for cAudio.

%package doc

Summary:       API documentation for cAudio

BuildArch:     noarch

%description doc

API documentation for cAudio, generated using doxygen.

%prep
%autosetup -p1

# Remove bundled dependencies
rm -rf Dependencies*

# Set /lib manually because this software has interesting ideas about how to use cmake
sed 's,/lib,/%{_lib},g' -i CMakeLists.txt
sed 's,LIBRARY DESTINATION lib,LIBRARY DESTINATION %{_lib},g' -i CMake/InstallDependencies.cmake

# Fix some spurious executable perm errors.
chmod -x cAudio/Headers/cAudioStaticSource.h
chmod -x cAudio/Headers/cOpenALUtil.h

%build
mkdir build
cd build

export CXXFLAGS="%{optflags} -Wl,--as-needed"

# There is a MPEG decoder plugin that uses code derived from ffmpeg; this can't be built in Fedora.
# There are also C# bindings. They do not compile: https://github.com/R4stl1n/cAudio/issues/42
# The EAX legacy preset plugin  builds and works fine. However, the .so is not currently versioned.
%cmake .. -DCAUDIO_SYSTEM_OGG=TRUE -DCAUDIO_BUILD_EAX_PLUGIN=TRUE -DCAUDIO_BUILD_MP3DECODER_PLUGIN=TRUE

make %{?_smp_mflags}

cd ../
doxygen

%install
cd build
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%{_libdir}/libcAudio.so.2
%{_libdir}/libcAudio.so.2.3.0

%{_libdir}/libEAXLegacyPreset.so.2
%{_libdir}/libEAXLegacyPreset.so.2.3.0

%{_libdir}/libcAp_mp3Decoder.so.2
%{_libdir}/libcAp_mp3Decoder.so.2.3.0

%license License.txt
%doc README.md

%files examples
%{_bindir}/Tutorial*

%files devel
%{_libdir}/libcAudio.so
%{_libdir}/libEAXLegacyPreset.so
%{_libdir}/libcAp_mp3Decoder.so
%{_includedir}/cAudio

%files doc
%doc Documentation/html
%license License.txt

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.3.1-6
- Also provide cAudio-freeworld.

* Tue May 23 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.3.1-5
- Now that it's allowed in Fedora, build the MP3 plugin in Fedora.
- Obsolete the cAudio-freeworld package from RPM Fusion.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Ben Rosser <rosser.bjr@gmail.com> 2.3.1-3
- Build libEAXLegacyPreset as part of cAudio.

* Tue Aug 16 2016 Ben Rosser <rosser.bjr@gmail.com> 2.3.1-2
- Fix bad macro (_isa should be ?_isa).
- Add license.txt to doc subpackage, since it doesn't require the main package.

* Sun Aug 14 2016 Ben Rosser <rosser.bjr@gmail.com> 2.3.1-1
- Update to latest upstream release.
- Upstream now versioning their own .so (but not plugins yet).
- As a result, temporarily removed libEAXLegacyPreset plugin.
- Patch for ogg/vorbis unbundling was accepted upstream.
- Add -Wl,--as-needed flags to fix unused-direct-shlib-dependency errors.
- Added graphviz as a build dependency.
- Streamlined installation of documentation files.
- Removed dependency on main package from -doc subpackage.

* Thu Jul 28 2016 Ben Rosser <rosser.bjr@gmail.com> 2.2.0-2
- Fix build of libEAXLegacyPreset plugin.
- Version both libcAudio.so and libEAXLegacyPreset.so downstream.
- Create doc subpackage for the cAudio documentation.

* Thu Jul 21 2016 Ben Rosser <rosser.bjr@gmail.com> 2.2.0-1
- Initial package.
- Unbundled libogg and libvorbis.
