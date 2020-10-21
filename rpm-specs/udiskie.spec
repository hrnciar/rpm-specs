Name:           udiskie
Version:        2.2.0
Release:        3%{?dist}
Summary:        Removable disk auto-mounter

License:        MIT
URL:            https://pypi.org/project/%{name}
Source0:        %{pypi_source}
Source1:        50-udiskie.rules

BuildArch:      noarch
BuildRequires:  asciidoc gettext
BuildRequires:  python3-devel python3-setuptools

# Require the module for the correct python
Requires: python3-%{name} = %{version}-%{release}

# Require package implementing required functionality
Requires: polkit hicolor-icon-theme

# Recommend tag not supported on EPEL
%if 0%{?!rhel}
# Recommended for full functionality
Recommends: libnotify
%endif

%description
%{name} is a front-end for UDisks written in python. Its main purpose is
automatically mounting removable media, such as CDs or flash drives. It has
optional mount notifications, a GTK tray icon and user level CLIs for manual
mounting and unmounting operations.

%package -n python3-%{name}
Summary: Python 3 module for udisks disk automounting
%global non_python_requires udisks2 gtk3 python3-gobject

BuildRequires: %{non_python_requires}
BuildRequires: %{py3_dist docopt PyYAML}
Requires: %{non_python_requires}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{name} is a front-end for UDisks written in python. This package provides the
python 3 modules used by the %{name} binaries.

%prep
%setup -q
find -name '*.txt' -exec chmod -x '{}' +
find -name '*.py' -exec sed -i 's|^#!python|#!%{__python3}|' '{}' +

# Make test folder into a proper module, if it already isn't
[ -f test/__init__.py ] || touch test/__init__.py

%build
%py3_build

# Build man page
%make_build -C doc

%install
%py3_install
find %{buildroot}%{python3_sitelib} -name '*.exe' -delete

# Install polkit rules
install -p -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/polkit-1/rules.d/50-%{name}.rules

# Install man page
install -d %{buildroot}%{_mandir}/man8
install -p -m644 -t %{buildroot}%{_mandir}/man8 doc/%{name}.8

# Create man pages for other binaries
for other in %{name}-mount %{name}-umount %{name}-info; do
  echo ".so man8/%{name}.8" > %{buildroot}%{_mandir}/man8/"${other}.8"
done

# Find all localization files
%find_lang %{name}

%check
# Only run tests with satisfied dependencies
%{__python3} setup.py test --test-suite test.test_match

%files -f %{name}.lang
%{_mandir}/man8/%{name}*.8*
%doc CONTRIBUTORS README.rst
%license COPYING
%config(noreplace) %{_sysconfdir}/polkit-1/rules.d/50-%{name}.rules
%{_bindir}/%{name}
%{_bindir}/%{name}-mount
%{_bindir}/%{name}-umount
%{_bindir}/%{name}-info
%{_datadir}/icons/hicolor/scalable/actions/%{name}*
%{_datadir}/zsh/site-functions/_%{name}*

%files -n python3-%{name}
%doc CONTRIBUTORS README.rst
%license COPYING
%{python3_sitelib}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Jan Staněk <jstanek@redhat.com> - 2.2.0-1
- Upgrade to version 2.2.0

* Fri Apr 17 2020 Jan Staněk <jstanek@redhat.com> - 2.1.1-1
- Upgrade to version 2.1.1

* Tue Feb 04 2020 Jan Staněk <jstanek@redhat.com> - 2.1.0-1
- Upgrade to version 2.1.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jan Staněk <jstanek@redhat.com> - 2.0.4-2
- Rebuilt with gating enabled.

* Tue Jan 21 2020 Jan Staněk <jstanek@redhat.com> - 2.0.4-1
- Upgrade to version 2.0.4

* Mon Jan 20 2020 Jan Staněk <jstanek@redhat.com> - 2.0.3-1
- Upgrade to version 2.0.3

* Thu Jan 02 2020 Jan Staněk <jstanek@redhat.com> - 2.0.2-1
- Upgrade to version 2.0.2
- Modernize and clean spec file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Jan Staněk <jstanek@redhat.com> - 1.7.7-1
- Upgrade to version 1.7.7

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.5-4
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.5-2
- Rebuilt for Python 3.7

* Thu May 24 2018 Jan Staněk <jstanek@redhat.com> - 1.7.5-1
- Upgrade to 1.7.5

* Mon May 21 2018 Jan Staněk <jstanek@redhat.com> - 1.7.4-1
- Upgrade to 1.7.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Jan Staněk <jstanek@redhat.com> - 1.7.3-1
- Upgrade to 1.7.3
- Drop deprecated python2 subpackage

* Wed Oct 11 2017 Jan Staněk <jstanek@redhat.com> - 1.7.1-2
- Renamed Python 2 dependencies to python2-*
- Generated man page for new udiskie-info binary

* Wed Oct 04 2017 Jan Staněk <jstanek@redhat.com> - 1.7.1-1
- Upgrade to 1.7.1

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.8-6
- Python 2 binary package renamed to python2-udiskie
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.8-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 10 2016 Jan Stanek <jstanek@redhat.com> - 1.4.8-1
- Update to 1.4.8

* Wed Feb 03 2016 Jan Stanek <jstanek@redhat.com> - 1.4.7-1
- Update to 1.4.7

* Wed Feb 03 2016 Jan Stanek <jstanek@redhat.com> - 1.4.1-2
- Fix build failures on EPEL7

* Mon Dec 21 2015 Jan Stanek <jstanek@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Jan Stanek <jstanek@redhat.com> - 1.3.2-1
- Update to 1.3.2

* Thu Sep 24 2015 Jan Stanek <jstanek@redhat.com> - 1.3.1-1
- Update to 1.3.1
- Add libnotify as weak dependency

* Thu Sep 03 2015 Jan Stanek <jstanek@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Tue Sep 01 2015 Jan Stanek <jstanek@redhat.com> - 1.2.1-1
- Update to 1.2.1.

* Thu Jun 04 2015 Jan Stanek <jstanek@redhat.com> - 1.2.0-1
- Initial package
