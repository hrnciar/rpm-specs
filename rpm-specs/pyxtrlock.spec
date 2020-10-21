Name:           pyxtrlock
Version:        0.2
Release:        24%{?dist}
Summary:        The X transparent screen lock rewritten in Python

License:        GPLv3+
URL:            https://zombofant.net/hacking/pyxtrlock
Source0:        https://github.com/leonnnn/pyxtrlock/archive/%{version}.tar.gz
Source1:        %{name}.png

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

# Note: explicit lib dependencies because these are used through python ctypes,
# hence not picked up automatically by rpm.
Requires:       libX11
Requires:       libxcb >= 1.4
Requires:       xcb-util-image
Requires:       python3-simplepam

%description
pyxtrlock, like its predecessor xtrlock, is a very minimal X display lock
program. While pyxtrlock is running, it does not obscure the screen, only the
mouse and keyboard are grabbed and the mouse cursor becomes a padlock. Output
displayed by X programs, and windows put up by new X clients, continue to be
visible, and any new output is displayed normally.

%prep
%setup -q


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}%{python3_sitelib}/*.egg-info

mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

cat >> %{buildroot}/%{name}.desktop << EOF
[Desktop Entry]
Name=pyxtrlock
Comment=Screen Lock
Encoding=UTF-8
Icon=%{name}
Exec=%{name}
Terminal=false
Type=Application
EOF

desktop-file-install \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{name}.desktop

cp -a %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/


%files
%doc README.md CHANGELOG COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2-23
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-21
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-20
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Feb 20 2014 Leon Weber <leon@leonweber.de> - 0.2.5
- Use cp -a for install to preserve timestamp

* Thu Feb 20 2014 Leon Weber <leon@leonweber.de> - 0.2-4
- Add note justifying explicit lib dependencies
- Use buildroot macro consistently
- Ship pyxtrlock icon
- Use mkdir -p without macro
- Remove egg file

* Wed Feb 19 2014 Leon Weber <leon@leonweber.de> - 0.2-3
- Add .desktop file

* Fri Feb 14 2014 Leon Weber <leon@leonweber.de> - 0.2-2
- Explicitly state library dependencies

* Tue Feb 11 2014 Leon Weber <leon@leonweber.de> - 0.2-1
- First version for Fedora
