Name:           lsp-plugins
Version:        1.1.26
Release:        2%{?dist}
Summary:        Linux Studio Plugins

License:        LGPLv3+ and zlib
URL:            https://lsp-plug.in/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
# Source0:        https://github.com/sadko4u/%{name}/releases/download/%{name}-%{version}/%{name}-src-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libstdc++-devel >= 4.7
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.5
BuildRequires:  lv2-devel >= 1.10
BuildRequires:  ladspa-devel >= 1.13
BuildRequires:  expat-devel >= 2.1
BuildRequires:  libsndfile-devel >= 1.0.25
BuildRequires:  cairo-devel >= 1.14
BuildRequires:  php >= 5.5.14
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libGL-devel
BuildRequires:  php-cli
BuildRequires:  desktop-file-utils

Requires:       redhat-menus
Requires:       hicolor-icon-theme

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
compatibles with LADSPA, LV2, LinuxVST formats and Standalone (using Jack).

%package doc
Summary:        Linux Studio Plugins documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for Linux Studio Plugins

%package ladspa
Summary:        Linux Studio Plugins LADSPA format
Requires:       ladspa%{?_isa}

%description ladspa
Linux Studio Plugins (LSP) compatible with the obsolete LADSPA format.

%package lv2
Summary:        Linux Studio Plugins LV2 format
Requires:       lv2%{?_isa}

%description lv2
Linux Studio Plugins (LSP) compatible with the LV2 format (recommended format).


%package vst
Summary:        Linux Studio Plugins VST format
Requires:       Carla-vst%{?_isa}

%description vst
Linux Studio Plugins (LSP) and UIs for Steinberg's VST 2.4 format ported on GNU/Linux Platform.

%package jack
Summary:        Linux Studio Plugins JACK format

%description jack
Linux Studio Plugins (LSP) standalone versions for JACK Audio connection Kit with UI


%prep
%autosetup -p1 -n %{name}-src-%{version}
sed -i 's|(PREFIX)/lib|(PREFIX)/%{_lib}|' Makefile
rm -rf include/3rdparty/ladspa
sed -i 's|-Wl,-rpath,$(LD_PATH)||' scripts/make/tools.mk


%build
%ifarch %ix86
%global optflags %{optflags} -DLSP_PROFILING
%endif
%{set_build_flags}
%make_build PREFIX=%{_prefix} SHELL="/bin/bash -x"



%install
%make_install PREFIX=%{_prefix}
mv %{buildroot}%{_datadir}/doc .

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{_sysconfdir}/xdg/menus/applications-merged/%{name}.menu
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/%{name}.directory
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files doc
%doc doc/%{name}/*

%files ladspa
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{_libdir}/ladspa/%{name}*

%files lv2
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{_libdir}/lv2/%{name}*

%files vst
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{_libdir}/vst/%{name}*

%files jack
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{_libdir}/%{name}


%changelog
* Thu Oct 01 2020 Jeff Law  <law@redhat.com> - 1.1.26-2
- Re-enable LTO

* Fri Sep 18 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.26-1
- Update to 1.1.26

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.24-1
- Update to 1.1.24

* Sun May 31 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.22-1
- Update to 1.1.22

* Thu Apr 23 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.19-1
- Update to 1.1.19

* Mon Apr 06 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.17-1
- Update to 1.1.17

* Sun Mar 29 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.15-1
- Update to 1.1.15

* Mon Mar 23 2020 Vasiliy Glazov <vascom2@gmail.com> - 1.1.14-1
- Update to 1.1.14

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.13-1
- Update to 1.1.13

* Mon Dec 23 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.11-1
- Update to 1.1.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.10-1
- Update to 1.1.10

* Thu Jun 27 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.9-2
- Corrected lisense
- Spec improvments

* Wed Jun 26 2019 Vasiliy Glazov <vascom2@gmail.com> - 1.1.9-1
- Initial release
