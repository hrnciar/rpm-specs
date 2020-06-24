%global uuid    com.leinardi.%{name}

Name:           gst
Version:        0.7.3
Release:        1%{?dist}
Summary:        System utility designed to stress and monitoring various hardware components

License:        GPLv3+
URL:            https://gitlab.com/leinardi/gst
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.45.1
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.56.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30
BuildRequires:  python3-devel

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       lm_sensors
Requires:       python3-gobject >= 3.34.0
Requires:       python3-humanfriendly >= 4.18
Requires:       python3-injector >= 0.18.2
Requires:       python3-matplotlib-gtk3 >= 3.1.1
Requires:       python3-peewee >= 3.13.1
#Requires:      python3-psutil >= 5.6.7
Requires:       python3-psutil
Requires:       python3-pyxdg >= 0.26
#Requires:      python3-pyyaml >= 5.3
Requires:       python3-pyyaml
Requires:       python3-requests >= 2.22.0
Requires:       python3-rx >= 3.0.1

Recommends:     dmidecode
Recommends:     stress-ng

%description
GST is a GTK system utility designed to stress and monitoring various hardware
components like CPU and RAM.

- Run different CPU and memory stress tests
- Run multi and single core benchmark
- Show Processor information (name, cores, threads, family, model, stepping,
  flags,bugs, etc)
- Show Processor's cache information
- Show Motherboard information (vendor, model, bios version, bios date, etc)
- Show RAM information (size, speed, rank, manufacturer, part number, etc)
- Show CPU usage (core %, user %, load avg, etc)
- Show Memory usage
- Show CPU's physical's core clock (current, min, max)
- Show Hardware monitor (info provided by sys/class/hwmon)


%prep
%autosetup
sed -e '/meson_post_install/d' -i meson.build


%build
%meson
%meson_build


%install
%meson_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING.txt
%doc CHANGELOG.md README.md RELEASING.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Mon Feb 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1
- Update to 0.7.1

* Sun Feb 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jan 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-5
- Add dep 'lm_sensors'

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-3
- Add dep 'dmidecode'

* Mon Jan 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-2
- Add dep 'stress-ng'

* Sun Jan 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Sun Jan 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-5
- Initial package
