%global         _with_cppunit 1

Name:           xournalpp
Version:        1.0.18
Release:        2%{?dist}
Summary:        Handwriting note-taking software with PDF annotation support

License:        GPLv2+
URL:            https://github.com/%{name}/%{name}
Source:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3 >= 3.10
BuildRequires:  desktop-file-utils
%{?_with_cppunit:
BuildRequires:  cppunit-devel >= 1.12-0
}
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(portaudiocpp) >= 12
BuildRequires:  pkgconfig(sndfile)
Requires:       hicolor-icon-theme
Requires:       %{name}-plugins = %{version}-%{release}
Requires:       %{name}-ui = %{version}-%{release}

%description
Xournal++ is a handwriting note-taking software with PDF annotation support.
Supports Pen input like Wacom Tablets

%package	plugins
Summary:        Default plugin for %{name}
BuildArch:      noarch

%description	plugins
The %{name}-plugins package contains sample plugins for  %{name}.

%package	ui
Summary:        User interface for %{name}
BuildArch:      noarch

%description	ui
The %{name}-ui package contains a graphical user interface for  %{name}.


%prep
%autosetup

#Fix tlh aka klingon language
mv po/tlh_AA.po po/tlh.po
sed -i 's|tlh-AA|tlh|g' po/tlh.po

%build
%cmake3 \
        %{_with_cppunit: -DENABLE_CPPUNIT=ON} \
        .

# Add translations parameter
# https://github.com/xournalpp/xournalpp/issues/1596
%make_build translations

%install
%make_install

#Remove depreciated key from desktop file
#Fix desktop file associated with application
desktop-file-install \
 --remove-key="Encoding" \
 --set-key="StartupWMClass" \
 --set-value="xournalpp" \
  %{buildroot}%{_datadir}/applications/com.github.%{name}.%{name}.desktop
%find_lang %{name}

#Remove scripts from icons interface
#rm -r %%{buildroot}%%{_datadir}/%%{name}/ui/icons/hicolor/update-icon-cache.sh
#rm -r %%{buildroot}%%{_datadir}/%%{name}/ui/iconsDark/hicolor/update-icon-cache.sh

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.%{name}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.%{name}.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/xournal-thumbnailer
%{_bindir}/%{name}
%{_datadir}/applications/com.github.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.github.%{name}.%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/*
%{_datadir}/mime/packages/com.github.%{name}.%{name}.xml
%exclude %{_datadir}/mimelnk/application/*
%{_datadir}/thumbnailers/com.github.%{name}.%{name}.thumbnailer
%dir %{_datadir}/%{name}
%{_metainfodir}/com.github.%{name}.%{name}.appdata.xml

%files plugins
%{_datadir}/%{name}/plugins

%files ui
%{_datadir}/%{name}/ui

%changelog
* Tue Apr 21 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.18-2
- Set value key on desktop file associated with application (#1826395)

* Thu Apr 16 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18 (#1824351)

* Tue Feb 04 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17 (#1798239)
- Drop unneeded texlive dependencies
- Fix build with translations parameter

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1.0.16-9
- Rebuild for poppler-0.84.0

* Sun Jan 12 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-8
- Remove depreciate key in desktop file

* Mon Dec 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-7
- Remove architecture requirement for plugins and ui

* Mon Dec 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-6
- Fix typos

* Mon Dec 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-5
- Fix architecture requirement for ui

* Wed Dec 11 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-4
- Review fixes

* Wed Dec 11 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-3
- Add hicolor-icon-theme to requirement
- Use desktop file validation
- Split xournal data share into subpackages
- Review fixes

* Sun Nov 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.16-2
- Remove scripts from ui icons directory
- Relocate tlh locale directory

* Sun Nov 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.16-1
- Release 1.0.16
- Enable cppunit

* Sun Nov 10 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.15-2
- Update spec file based on review
- Include appstream data

* Sun Nov 10 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.15-1
- Release 1.0.15

* Tue Aug 13 2019 dfas <d.dfas@moens.cc> - 1.0.13-2.git7349762
- Release 1.0.13-current

* Tue Jun 25 2019 dfas <d.dfas@moens.cc> - 1.0.13-1.gita7f0275
- Release 1.0.13-current

* Fri May 3 2019 Francisco Gonzalez <gzmorell@gmail.com> - 1.0.10-1
- First attempt at packaging xournalpp.
