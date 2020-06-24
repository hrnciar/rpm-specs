# Pre-release
#%%global git_tag 2.1.0rc3

%global git_tag %{version}

Name:           gns3-gui
Version:        2.2.9
Release:        1%{?dist}
Summary:        GNS3 graphical user interface

License:        GPLv3+
URL:            http://gns3.com
Source0:        https://github.com/GNS3/%{name}/archive/v%{git_tag}/%{name}-%{git_tag}.tar.gz
Source3:        %{name}.appdata.xml

BuildArch:      noarch

BuildRequires:  python3-devel 
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires: telnet 
Requires: cpulimit 
Requires: socat
Requires: python3-jsonschema 
Requires: python3-raven 
Requires: python3-psutil 
Requires: python3-qt5
Requires: gns3-net-converter >= 1.3.0

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

This package contains the client graphical user interface.

%prep
%autosetup -n %{name}-%{git_tag}

# Relax strict reqs
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/sentry-sdk.*//g' requirements.txt

# Disable update alerts
sed -i 's/"check_for_update": True,/"check_for_update": False,/' gns3/settings.py

# Disable anonymous data collection
sed -i 's/"send_stats": True,/"send_stats": False,/' gns3/settings.py

%build
%py3_build

%install
%py3_install

# Remove shebang
for lib in `find %{buildroot}/%{python3_sitelib}/ -name '*.py'`; do
 echo $lib
 sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done

# Remove empty files
find %{buildroot}/%{python3_sitelib}/ -name '.keep' -type f -delete

# Remove exec perm
find %{buildroot}/%{python3_sitelib}/ -type f -exec chmod -x {} \;

# AppData
mkdir -p %{buildroot}/%{_datadir}/appdata/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/appdata/


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/gns3*.desktop


%files 
%license LICENSE
%doc README.rst AUTHORS CHANGELOG
%{python3_sitelib}/gns3/
%{python3_sitelib}/gns3_gui*.egg-info/
%{_bindir}/gns3
%{_datadir}/applications/gns3*.desktop
%{_datadir}/icons/hicolor/*/apps/*gns3*
%{_datadir}/icons/hicolor/*/mimetypes/*-gns3*
%{_datadir}/mime/packages/gns3-gui.xml
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Fri Jun 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.9-1
- Update to 2.2.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.7-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.6-1
- Update to 2.2.6
- Drop duplicate desktop entry

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.20-1
- Update to 2.1.20

* Wed Sep 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.1.16-5
- drop dep on python3-sip

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-2
- Relax strict reqs

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-1
- Update to 2.1.16 (rhbz #1668653 #1668654)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.11-2
- Add missing PyQt dep

* Sat Nov 17 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.112.1.11-11
- Update to 2.1.11 (rhbz #1581506)

* Wed Jul 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8 (rhbz #1581506)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.5-2
- Rebuilt for Python 3.7

* Sat Apr 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5 (rhbz #1569275)

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (rhbz #1554315)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (rhbz #1536428)

* Thu Jan 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2 (rhbz #1532421)
- Disable anonymous data collection

* Sat Dec 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (rhbz #1528825)

* Mon Nov 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 final

* Sat Nov 04 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc3
- Update to 2.1.0-0.rc3

* Sun Oct 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc1
- Update to 2.1.0 RC1
- Fix appdata

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-2
- Disable update alert

* Sat Jul 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Sat May 13 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-2
- Update files section

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Fri Apr 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Sat Apr 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-2
- Rebuild for Python 3.6

* Sun Sep 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Fri Aug 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-2
- Fix appdata

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1
- Fix the url

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Minor spec fixes
- Provide AppData

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Initial spec 
