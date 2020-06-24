%global commit ff73e5a0880f6b5c5feceaf531b9dc73406f550a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global prerelease 20150506

Name:           lv2-artyfx-plugins
Version:        1.3
Release:        0.14.%{prerelease}git%{shortcommit}%{?dist}
Summary:        A collection of LV2 RT plugins

License:        GPLv2+
URL:            http://openavproductions.com/ArtyFX/
Source0:        https://github.com/harryhaaren/openAV-ArtyFX/archive/%{commit}.zip

BuildRequires:  faust
BuildRequires:  gcc-c++
BuildRequires:  non-ntk-devel
BuildRequires:  libsndfile-devel
BuildRequires:  cairomm-devel
BuildRequires:  lv2-devel
BuildRequires:  cmake
BuildRequires:  jack-audio-connection-kit-devel
Requires:       lv2

%global __provides_exclude_from ^%{_libdir}/lv2/.*$

%description
Arty FX is a plugin bundle of artistic "RT" effects. The aim of this plugin 
collection is to allow the designing of your sound just as you desired using
a fast, efficient workflow.

%prep
%setup -q -n openAV-ArtyFX-%{commit}
sed -i -e 's|\-Wall|%{optflags}|g' -e 's|lib/lv2||g' CMakeLists.txt
sed -i -e 's|-msse2 -mfpmath=sse||g' CMakeLists.txt

%build
%{cmake} 
make %{?_smp_mflags}

%install
install -d -m 0755 %{buildroot}/%{_libdir}/lv2
make install DESTDIR=%{buildroot}/%{_libdir}/lv2

%files
%doc CHANGELOG README.md
%license LICENSE
%{_libdir}/lv2/*.lv2

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.14.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.13.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.12.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.11.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.10.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.9.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.8.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.7.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-0.6.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-0.5.20150506gitff73e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Brendan Jones <brendan.jones.it@gmail.com> 1.3-0.4.20150506gitff73e5a0
- Remove sse all arches, correct changelog

* Wed May 06 2015 Brendan Jones <brendan.jones.it@gmail.com> 1.3-0.3.20150506gitff73e5a0
- Add missing BR

* Wed May 06 2015 Brendan Jones <brendan.jones.it@gmail.com> 1.1-0.4.20150506gitff73e5a0
- Update to latest git version

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-0.4.20140317git1dc4f00
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.3.20140317git1dc4f00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.2.20140317git1dc4f00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.1-0.1.git
- 1.1 Update, new plugins

* Sun Oct 27 2013 Brendan Jones <brendan.jones.it@gmail.com> 0-1.2.20131013git918613f
- Filter plugin from provides

* Sun Oct 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 0-1.1.20131013git918613f
- New upstream release contains LICENSE file

* Fri Oct 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0-0.1.20131011gita4d52ec
- Initial creation

