%global optflags        %{optflags} -flto=auto
%global build_ldflags   %{build_ldflags} -flto

Name:           pulseeffects
Version:        4.7.2
Release:        1%{?dist}
Summary:        Audio equalizer, filters and effects for Pulseaudio applications

License:        GPLv3+
Url:            https://github.com/wwmm/pulseeffects
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  boost-devel >= 1.70
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.56
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.12.5
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.12.5
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpulse) >= 11.0
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  zita-convolver-devel >= 3.1.0

Requires:       hicolor-icon-theme
Requires:       dbus-common
Requires:       gstreamer1-plugins-good >= 1.12.5
#Requires:       ladspa-swh-plugins >= 0.4
Requires:       lv2-calf-plugins >= 0.90.0
Requires:       ladspa-calf-plugins
Requires:       lv2-mdala-plugins
Requires:       lsp-plugins-lv2
Requires:       gstreamer1-plugins-bad-free-extras

Recommends:     zam-plugins
Recommends:     lv2-zam-plugins
Recommends:     ladspa-zam-plugins
Recommends:     rubberband


%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer many more effects for PulseAudio applications.

%prep
%autosetup
sed -i 's|#include <sigc++/sigc++.h>|#include <sigc++/sigc++.h>\n#include <string>|' include/plugin_base.hpp

%build
export LC_ALL="${LC_ALL:-UTF-8}"
%meson
%meson_build

%install
%meson_install

desktop-file-install %{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop \
--dir=%{buildroot}%{_datadir}/applications

%find_lang %{name}

# Change absolute symlinks to relative
# https://github.com/wwmm/pulseeffects/issues/590
find %{buildroot}%{_datadir}/help/ -type l -exec ln -sf ../../../C/pulseeffects/figures/{} {} \;


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.wwmm.%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/com.github.wwmm.%{name}.appdata.xml
%{_datadir}/help/*/%{name}
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service
%{_libdir}/gstreamer-1.0/libgst*.so


%changelog
* Wed Jun 03 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 4.7.2-1
- Update to 4.7.2

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 4.7.1-3
- Rebuilt for Boost 1.73

* Mon May 11 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 4.7.1-2
- Enable loudness plugin

* Thu Mar 12 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 4.7.1-1
- Update to 4.7.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Fri Nov 29 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 4.6.9-1
- Update to 4.6.9

* Wed Sep 18 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.6.8-1
- Update to 4.6.8
- Drop lv2-mdala-plugins

* Tue Aug 13 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.6.6-1
- Update to 4.6.6
- Enable LTO

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.6.5-4
- Added Requires for crossfeed plugin

* Fri Jun 28 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.6.5-3
- Added Requires lsp-plugins-lv2

* Wed Jun 26 07:54:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.6.5-2
- Rebuild for new zita-convolver

* Tue Jun 25 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.6.5-1
- Update to 4.6.5

* Fri Jun 21 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.6.4-1
- Update to 4.6.4

* Tue Feb 12 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.5.0-1
- Initial release for Fedora
