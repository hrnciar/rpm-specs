Name:           sepolicy_analysis
Version:        0.1
Release:        12%{?dist}
Summary:        SELinux policy analysis tool

License:        GPLv3
URL:            https://github.com/vmojzis/sepolicy_analysis
#./setup.py egg_info --egg-base /tmp sdist
Source0:        https://github.com/vmojzis/sepolicy_analysis/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

Requires: python3-setools >= 4.0
Requires: python3-networkx >= 1.11

%description
Tool designed to help increase the quality of SELinux policy by identifying
possibly dangerous permission pathways, simplifying regression testing and
providing policy visualization.

%prep
%autosetup

%build
%py3_build

%install
#mkdir -p % {buildroot}% {_mandir}/man1
%py3_install

%check
%if %{?_with_check:1}%{!?_with_check:0}
%{__python3} setup.py test
%endif

%files
%license COPYING
%{python3_sitelib}/*
%{_bindir}/seextract_cil
%{_bindir}/sebuild_graph
%{_bindir}/seexport_graph
%{_bindir}/segraph_query
%{_bindir}/sevisual_query
%dir %{_sysconfdir}/sepolicyanalysis
%config(noreplace) %{_sysconfdir}/sepolicyanalysis/domain_groups_cil.conf
%config(noreplace) %{_sysconfdir}/sepolicyanalysis/security_related.conf
%doc %{_mandir}/man1/se*

%changelog
* Thu Jun 04 2020 Vit Mojzis <vmojzis@redhat.com> - 0.1-12
- Add dependency on python3-networkx
- Fix setools dependency (setools-python3 got renamed to python3-setools)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Vit Mojzis <vmojzis@redhat.com> - 0.1-1
- Initial release

