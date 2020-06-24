Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    0.0.11
Release:    5%{?dist}
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/dib-utils
Source0:    http://tarballs.openstack.org/dib-utils/dib-utils-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-d2to1
BuildRequires: python3-pbr

Conflicts: diskimage-builder < 0.1.15
Obsoletes: dib-utils < %{version}-%{release}

%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%prep
%setup -q -n %{name}-%{version}

%build
%py3_build

%install
%py3_install


%files
%doc README.md
%{_bindir}/dib-run-parts
%{python3_sitelib}/dib_utils*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.11-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.11-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Alfredo Moralejo <amoralej@redhat.com> - 0.0.11-1
- Update to 0.0.11

* Wed Feb 27 2019 Yatin Karel <ykarel@redhat.com> - 0.0.9-10
- Build python3 instead of python2 as python2 is being removed

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.9-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Mike Burns <mburns@redhat.com> 0.0.9-1
- Update to upstream 0.0.9

* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.0.8-1
- Update to upstream 0.0.8

* Wed Oct 01 2014 James Slagle <jslagle@redhat.com> 0.0.7-1
- Update to upstream 0.0.7

* Thu Sep 18 2014 James Slagle <jslagle@redhat.com> - 0.0.6-3
- Add patch to update dib-run-parts to fix sourcing of environment.d files

* Wed Sep 17 2014 James Slagle <jslagle@redhat.com> - 0.0.6-2
- Add python BuildRequires

* Wed Sep 17 2014 James Slagle <jslagle@redhat.com> - 0.0.6-1
- Rebase on upstream dib-utils.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Ben Nemec <bnemec@redhat.com> - 0.0.0-1
- Initial package creation
