Name:           mu
Version:        1.0.3
Release:        4%{?dist}
Summary:        A simple Python editor not only for micro:bit
License:        GPLv3
URL:            https://github.com/mu-editor/mu
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(microfs) >= 1.3
BuildRequires:  python3dist(nudatus)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pyflakes)
BuildRequires:  python3dist(pyqtchart)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(qtconsole)
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(uflash)
# no dist provide for this:
BuildRequires:  python3-qt5
BuildRequires:  python3-qscintilla-qt5

BuildRequires:  systemd

BuildRequires:  qt5-qtserialport >= 5.5.0

BuildRequires:  %{_bindir}/desktop-file-install
BuildRequires:  %{_bindir}/xvfb-run

%?python_enable_dependency_generator

# unbundled
Requires:       python3dist(microfs) >= 1.3
Requires:       python3dist(nudatus)
Requires:       python3dist(uflash)
# no dist provide for this:
Requires:       python3-qt5 >= 5.11
Requires:       python3-qscintilla-qt5 >= 2.10.7

Requires:       hicolor-icon-theme

# The name on PyPI and the Shell command
Provides:       mu-editor = %{version}-%{release}

%description
mu is a simple Python editor also for BBC micro:bit devices.

%prep
%autosetup -p1

# make the versions not pinned for the entry_point to work
# also pyqt and qscintilla are not properly provided in Fedora :(
# upstream removes some reqs on arm, we don't
sed -i -e 's/pycodestyle==2.4.0/pycodestyle >= 2.4, < 2.7/' \
       -e 's/pyflakes==2.0.0/pyflakes >= 2.0, < 2.3/' \
       -e 's/pyserial==3.4/pyserial >= 3.0, < 3.5/' \
       -e 's/qtconsole==4.3.1/qtconsole >= 4.3, < 5/' \
       -e 's/matplotlib==2.2.2/matplotlib >= 2.2, < 4/' \
       -e 's/pgzero==1.2/pgzero >= 1.2, < 1.3/' \
       -e 's/PyQtChart==5.14.0/PyQtChart >= 5.11, < 6/' \
       -e "s/'pyqt5==5.14.1', 'qscintilla==2.11.4',//" \
       -e "s/machine.lower().startswith('arm')/False/" \
       setup.py

# unbundle things
sed -i 's/from mu.contrib import /import /' mu/modes/microbit.py tests/modes/test_microbit.py
rm -rf mu/contrib
sed -i "s@ 'mu.contrib',@@" setup.py
sed -i "s@mu.contrib.@@" tests/modes/test_microbit.py


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/applications \
         %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ \
         %{buildroot}%{_udevrulesdir} \
         %{buildroot}%{_metainfodir}

# Make sure we have the -s flag
# https://bugzilla.redhat.com/show_bug.cgi?id=1799790
pathfix.py -pni "%{python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/*

desktop-file-install --dir=%{buildroot}%{_datadir}/applications conf/mu.codewith.editor.desktop
cp -p conf/mu.codewith.editor.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -p conf/90-usb-microbit.rules %{buildroot}%{_udevrulesdir}/
cp -p conf/mu.appdata.xml %{buildroot}%{_metainfodir}/


%check
xvfb-run %{__python3} -m pytest -vv tests


%files
%doc README.rst LICENSE
%{_bindir}/mu-editor
%{python3_sitelib}/mu*/
%{_udevrulesdir}/90-usb-microbit.rules
%{_datadir}/icons/hicolor/256x256/apps/mu.codewith.editor.png
%{_datadir}/applications/mu.codewith.editor.desktop
%{_metainfodir}/mu.appdata.xml


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Allow pyflakes 2.2 and pycodestyle 2.6 (#1841648)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-1
- Update to 1.0.3
- Provide mu-editor

* Thu Feb 06 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-8
- Adapt the shebang to use the -s flag and only use system installed modules (#1799790)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Relax the dependency version restrictions for matplotlib

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Relax the dependency version restrictions even further (#1731655)

* Sun Mar 24 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-1
- Update to 1.0.2
- Loosen some strict dependency declarations
- Fix test failure

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Mu works with matplotlib 3.0

* Thu Sep 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Fix requires to allow startup
- Fix the desktop file

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1387943)
- Move udev rules to /usr/lib/udev/rules.d (#1602361)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-3
- Rebuilt for Python 3.7

* Sun May 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-2
- Add missing requires (pyflakes, pep8) (#1582237)

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-1
- Updated to 0.9.13
- Unbundle things
- Run tests

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 13 2016 Kushal Das <kushal@fedoraprojects.org> - 0.2-1
- Updates to 0.2 release

* Fri Feb 26 2016 Kushal Das <kushal@fedoraprojects.org> - 0.1-2
- Updates the desktop file creation

* Tue Feb 02 2016 Kushal Das <kushal@fedoraprojects.org> - 0.1-1
- Initial package creation
