Name:           mimic
Version:        1.3.0.1
Release:        4%{?dist}
Summary:        Mycroft's TTS engine

License:        BSD
URL:            https://mimic.mycroft.ai/
Source0:        https://github.com/MycroftAI/mimic/archive/%{version}.tar.gz
Patch0:         mimic-fix-pulse.patch

BuildRequires:  automake autoconf libtool
BuildRequires:  alsa-lib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  pulseaudio-libs-devel


%description
Mimic is a fast, lightweight Text-to-speech engine developed by Mycroft A.I. 
and VocalID, based on Carnegie Mellon University’s FLITE software. Mimic takes 
in text and reads it out loud to create a high quality voice. Mimic's 
low-latency, small resource footprint, and good quality voices set it apart 
from other open source text-to-speech projects.

%package devel
Summary: Development files for Mimic
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Mimic, a small, fast speech synthesis engine.


%prep
%autosetup -p1 -n %{name}1-%{version}

%build
# This package triggers a fault in GCC when building with LTO enabled.
# Disable LTO until GCC is fixed
%define _lto_cflags %{nil}

autoreconf -vif
%configure --enable-shared --with-audio=alsa --with-audio=pulseaudio
%{make_build}

%install
%{make_install}

# Remove static libraries and libtool archives
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.la" -delete


%ldconfig_scriptlets


%files
%license COPYING
%doc ACKNOWLEDGEMENTS
%{_libdir}/libttsmimic*.so.*
%{_bindir}/mimic*
%{_bindir}/compile_regexes
%{_bindir}/t2p
%{_datadir}/man/man1/mimic.1.gz
%{_datadir}/%{name}

%files devel
%{_libdir}/libttsmimic*.so
%{_libdir}/pkgconfig/mimic.pc
%{_includedir}/ttsmimic

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 1.3.0.1-2
- Disable LTO

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0.1-1
- New upstream 1.3.0.1

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0.0-1
- New upstream 1.3.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-13
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0.2-11
- Fix building against PulseAudio 1.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-9
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-7
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-6
- Rebuild for ICU 61.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-4
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0.2-1
- New upstream 1.2.0.2
- Package review updates

* Fri Oct 28 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-1
- Initial package
