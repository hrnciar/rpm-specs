%global pkgname m2r
%global desc M2R converts a markdown file including reST markups to a valid reST format.

Name:           python-%{pkgname}
Version:        0.2.0
Release:        12%{?dist}
Summary:        Markdown to reStructuredText converter

License:        MIT
URL:            https://github.com/miyakogi/%{pkgname}
Source0:        https://github.com/miyakogi/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

Patch0:         sphinx-3.patch
Patch1:         sphinx-code-block.patch

BuildArch:      noarch


%description
%{desc}


%package -n python3-%{pkgname}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-docutils
BuildRequires:  python3-mistune
BuildRequires:  python3-pygments
BuildRequires:  python3-mock
Requires:       python3-docutils
Requires:       python3-mistune
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname}
%{desc}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Remove upstream's egg-info
rm -rf %{pkgname}.egg-info

# Remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' m2r.py


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=$(pwd) %{__python3} setup.py test -s tests


%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{_bindir}/m2r
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pkgname}.py
%{python3_sitelib}/%{pkgname}-%{version}*-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/tests


%changelog
* Fri Aug 21 2020 Nikola Forró <nforro@redhat.com> - 0.2.0-12
- Explicitly build-require setuptools

* Thu Aug 20 2020 Nikola Forró <nforro@redhat.com> - 0.2.0-11
- Use reST literal block for Sphinx code block
  resolves: #1870105

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-9
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Nikola Forró <nforro@redhat.com> - 0.2.0-8
- Fix Sphinx 3 compatibility
  resolves: #1823514

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Nikola Forró <nforro@redhat.com> - 0.2.0-6
- Remove Python 2 subpackage
  resolves: #1769838

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Nikola Forró <nforro@redhat.com> - 0.2.0-1
- Update to 0.2.0
  resolves: #1615361

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Nikola Forró <nforro@redhat.com> - 0.1.15-1
- Update to 0.1.15
  resolves: #1597056

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.14-2
- Rebuilt for Python 3.7

* Thu Mar 22 2018 Nikola Forró <nforro@redhat.com> - 0.1.14-1
- Update to 0.1.14
  resolves: #1559372

* Wed Feb 14 2018 Nikola Forró <nforro@redhat.com> - 0.1.13-1
- Update to 0.1.13
  resolves: #1545220

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Nikola Forró <nforro@redhat.com> - 0.1.12-2
- Use more descriptive source tarball name
- Fix python2 dependency names

* Wed Sep 13 2017 Nikola Forró <nforro@redhat.com> - 0.1.12-1
- Update to 0.1.12
  resolves: #1490365

* Wed Aug 30 2017 Nikola Forró <nforro@redhat.com> - 0.1.11-1
- Update to 0.1.11
  resolves: #1486504

* Fri Aug 25 2017 Nikola Forró <nforro@redhat.com> - 0.1.10-2
- Add missing dist tag

* Tue Aug 15 2017 Nikola Forró <nforro@redhat.com> - 0.1.10-1
- Update to 0.1.10
- Switch to release versioning
  resolves: #1480575

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2.git8e4ce37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Nikola Forró <nforro@redhat.com> - 0.1.7-1.git8e4ce37
- Update to 0.1.7
  resolves: #1473289

* Wed May 31 2017 Nikola Forró <nforro@redhat.com> - 0.1.6-1.git871d579
- Update to 0.1.6
  resolves: #1457165

* Wed May 17 2017 Nikola Forró <nforro@redhat.com> - 0.1.5-2.git539a079
- Make image_link regex non-greedy

* Tue May 16 2017 Nikola Forró <nforro@redhat.com> - 0.1.5-1.git539a079
- Initial package
