
%global commit cfbd4b36165f1708b885610fa32775f75997579a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global prerelease 20150303

Name:           lv2-fabla
Version:        1.3
Release:        0.13.%{prerelease}git%{shortcommit}%{?dist}
Summary:        An LV2 drum sequencer

License:        GPLv2+
URL:            http://openavproductions.com/fabla/
Source0:        https://github.com/harryhaaren/openAV-Fabla/archive/%{commit}.zip

BuildRequires:  faust
BuildRequires:  gcc-c++
BuildRequires:  non-ntk-devel
BuildRequires:  libsndfile-devel
BuildRequires:  cairomm-devel
BuildRequires:  lv2-devel
BuildRequires:  cmake
Requires:       lv2

%description
%{name} is a drum sampler plugin instrument. It is ideal for loading up your
favorite sampled sounds and bashing away on a MIDI controller. Or if it’s 
crafty beat programming your after that’s cool too! The ADSR envelope allows
the shaping of hi-hats and kicks while the compressor beefs up the sound for 
those thumping kicks!
Additional presets can be found at:
   https://github.com/harryhaaren/openAV-presets

%prep
%setup -q -n openAV-Fabla-%{commit}
sed -i -e  's|lib/|%{_lib}/|g'  -e 's|\-Wall|%{optflags}|g' CMakeLists.txt
%ifnarch %{ix86} x86_64
sed -i -e 's|-msse2 -mfpmath=sse||g' CMakeLists.txt
%endif

%build
%cmake .
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_libdir}/lv2
make install DESTDIR=%{buildroot}

%files
%doc README.md CHANGELOG
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.11.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.3-0.10.20150303gitcfbd4b3
- Append curdir to CMake invokation. (#1668512)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.9.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.8.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.7.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.6.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.5.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.4.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.3-0.3.20150303gitcfbd4b3
- Disable SSE on all non x86(-64) architectures - rhbz#1220294
- Change order of CMakeLists.txt mangling to keep /usr/lib for hardening rules file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.2.20150303gitcfbd4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Brendan Jones <brendan.jones.it@gmail.com> 1.3-0.1.gitcfbd4b36
- Update to latest git 

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-4.3.20131003git5f2cb26
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.3.20131003git5f2cb26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2.3.20131003git5f2cb26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.3.20131003git5f2cb26
- Remove additional presets, update description

* Fri Oct 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.2.20101003git5f2cb26
- Remove durtySouth kit

* Sun Oct 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.1.20131003git5f2cb26
- Clean up git URLs and sources
- Split presets into separate package

* Tue Sep 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.1.gite8fb937
- Initial package

