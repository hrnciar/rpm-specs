Name:           alot
Version:        0.8.1
Release:        8%{?dist}
Summary:        Experimental terminal MUA based on notmuch mail

License:        GPLv3+
URL:            https://github.com/pazz/alot
Source0:        %{url}/archive/%{version}/%{version}.tar.gz
Patch0:         0001-don-t-depend-on-weird-python-magic-distribution.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
Requires:       python3-notmuch >= 0.27
Requires:       python3-urwid >= 1.3.0
Requires:       python3-urwidtrees >= 1.0
Requires:       python3-twisted >= 10.2.0
Requires:       python3-magic
Requires:       python3-configobj >= 4.7.0
Requires:       python3-gpg

%description
alot makes use of existing solutions where possible: It does not fetch, send or
edit mails; it lets notmuch handle your mailindex and uses a toolkit to render
its display. You are responsible for automatic initial tagging.

%prep
%autosetup -p1

%build
%py3_build
%make_build man SPHINX_BUILD=sphinx-build-3 PYTHON=python3 -C docs

%install
%py3_install
install -Dpm0644 docs/build/man/alot.1* -t %{buildroot}%{_mandir}/man1/

%files
%license COPYING
%doc NEWS README.md
%{python3_sitelib}/alot/
%{python3_sitelib}/alot-*.egg-info/
%{_bindir}/alot
%{_mandir}/man1/alot.1*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.8.1-1
- Update to 0.8.1
- s/python 2/python 3/
- Clean spec a bit.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.7-1
- Update to 0.7

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6-1
- Update to 0.6
- Cleanup spec

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.4-1
- update to 0.4

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.6-5
- Rebuild for gpgme 1.18

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 12 2014 Tomas Tomecek <ttomecek@redhat.com> - 0.3.6-1
- initial package

