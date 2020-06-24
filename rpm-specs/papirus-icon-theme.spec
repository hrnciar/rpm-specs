Name:           papirus-icon-theme
Version:        20200602
Release:        1%{?dist}
Summary:        Free and open source SVG icon theme based on Paper Icon Set

# Some icons are based on Paper Icon Theme, CC-BY-SA
# The rest is GPLv3
License:        GPLv3 and CC-BY-SA
URL:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE colorscheme support, Folder Color support, and others.

Papirus icon theme is available in six variants:

 - Papirus (for Arc / Arc Darker)
 - Papirus Dark (for Arc Dark)
 - Papirus Light (light theme with Breeze colors)
 - Papirus Adapta (for Adapta)
 - Papirus Adapta Nokto (for Adapta Nokto)
 - ePapirus (for elementary OS and Pantheon Desktop)

%prep
%autosetup

%build
# Nothing to build

%install
%make_install

export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    mkdir -p %{buildroot}%{_datadir}/icons/$t
    /bin/touch %{buildroot}%{_datadir}/icons/$t/icon-theme.cache
done

# Handle folder to link upgrade
# Remove in F33
%pretrans -p <lua>
-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
pathlist = {"%{_datadir}/icons/Papirus-Light/16x16/actions",
            "%{_datadir}/icons/Papirus-Light/16x16/devices",
            "%{_datadir}/icons/Papirus-Light/16x16/places",
            "%{_datadir}/icons/Papirus-Light/22x22/actions",
            "%{_datadir}/icons/Papirus-Light/24x24/actions"}
for key,path in ipairs(pathlist)
do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end

%post
export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%postun
export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    if [ $1 -eq 0 ] ; then
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    fi
done

%posttrans
export THEMES="ePapirus Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done

%files
%license LICENSE
%doc AUTHORS README.md
%{_datadir}/icons/ePapirus
%{_datadir}/icons/Papirus
%{_datadir}/icons/Papirus-Adapta
%{_datadir}/icons/Papirus-Adapta-Nokto
%{_datadir}/icons/Papirus-Dark
%{_datadir}/icons/Papirus-Light
%ghost %{_datadir}/icons/ePapirus/icon-theme.cache
%ghost %{_datadir}/icons/Papirus/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Adapta/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Adapta-Nokto/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Light/icon-theme.cache
# Handle folder to link upgrade
# Remove in F33
%ghost %{_datadir}/icons/Papirus-Light/16x16/actions.rpmmoved
%ghost %{_datadir}/icons/Papirus-Light/16x16/devices.rpmmoved
%ghost %{_datadir}/icons/Papirus-Light/16x16/places.rpmmoved
%ghost %{_datadir}/icons/Papirus-Light/22x22/actions.rpmmoved
%ghost %{_datadir}/icons/Papirus-Light/24x24/actions.rpmmoved

%changelog
* Thu Jun 18 15:31:28 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20200602-1
- Update to 20200602 (#1821029)

* Mon Mar 02 19:59:31 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20200301-1
- Update to 20200301

* Thu Feb 27 02:13:17 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20200201-1
- Update to 20200201

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 22:28:21 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20200102-1
- Release 20200102 (#1787866)

* Fri Dec 06 00:03:00 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20191101-1
- Release 20191101 (#1767767)

* Fri Oct 11 20:03:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20191009-1
- Release 20191009 (#1760661)

* Thu Oct 10 22:56:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190919-1
- Release 20190919

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 19:29:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190708-1
- Release 20190708

* Fri Jul 05 21:04:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190701-1
- Release 20190701 (#1725696)

* Sun Jun 16 15:25:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190615-1
- Release 20190615 (#1720826)

* Thu May 30 15:55:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190521-1
- Release 20190521 (#1712816)

* Sat May 04 18:35:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190501-1
- Release 20190501 (#1694640)

* Wed Mar 13 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190302-2
- Fix to handle folder to link upgrade

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 20190302-1
- Release 20190302 (#1687463)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 20181007-1
- Update to release 20181007

* Tue Oct 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 20180816-1
- Initial release
