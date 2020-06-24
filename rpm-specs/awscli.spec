Name:           awscli
Version:        1.18.85
Release:        1%{?dist}
Summary:        Universal Command Line Environment for AWS

License:        ASL 2.0 and MIT
URL:            https://aws.amazon.com/cli/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     groff
Requires:       python3-docutils

%{?python_provide:%python_provide python3-%{name}}

%description
This package provides a unified
command line interface to Amazon Web Services.

%prep
%autosetup -n %{name}-%{version} -p 1
rm -vr %{name}.egg-info
# https://github.com/aws/aws-cli/pull/4929
sed -i -e '/PyYAML/s/5.3/5.4/' setup.{py,cfg}
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +

# https://github.com/aws/aws-cli/issues/4837
sed -i "/,<0.16/d" setup.cfg
sed -i "/,<0.16/d" setup.py

%build
%py3_build

%install
%py3_install
rm -vf %{buildroot}%{_bindir}/{aws_bash_completer,aws_zsh_completer.sh,aws.cmd}
install -Dpm0644 bin/aws_bash_completer \
  %{buildroot}%{_datadir}/bash-completion/completions/aws
install -Dpm0644 bin/aws_zsh_completer.sh \
  %{buildroot}%{_datadir}/zsh/site-functions/_awscli

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/aws
%{_bindir}/aws_completer
%{python3_sitelib}/awscli/
%{python3_sitelib}/%{name}-*.egg-info/
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/aws
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_awscli

%changelog
* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.85-1
- 1.18.85

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.84-1
- 1.18.84

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.83-1
- 1.18.83

* Thu Jun 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.82-1
- 1.18.82

* Wed Jun 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.81-1
- 1.18.81

* Tue Jun 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.80-1
- 1.18.80

* Sat Jun 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.79-1
- 1.18.79

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.78-1
- 1.18.78

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.77-1
- 1.18.77

* Sat Jun 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.74-1
- 1.18.74

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.73-1
- 1.18.73

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.72-1
- 1.18.72

* Tue Jun 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.70-1
- 1.18.70

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.69-1
- 1.18.69

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.18.66-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.66-1
- 1.18.66

* Thu May 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.65-1
- 1.18.65

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.64-1
- 1.18.64

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.61-1
- 1.18.61

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.60-1
- 1.18.60

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.59-1
- 1.18.59

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.58-1
- 1.18.58

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.57-1
- 1.18.57

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.56-1
- 1.18.56

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.55-1
- 1.18.55

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.54-1
- 1.18.54

* Wed May 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.53-1
- 1.18.53

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.52-2
- Patch for docutils version issue.

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.52-1
- 1.18.52

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.51-1
- 1.18.51

* Fri May 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.50-1
- 1.18.50

* Thu Apr 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.49-1
- 1.18.49

* Wed Apr 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.48-1
- 1.18.48

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.47-1
- 1.18.47

* Sat Apr 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.46-1
- 1.18.46

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.45-1
- 1.18.45

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.44-1
- 1.18.44

* Wed Apr 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.43-1
- 1.18.43

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.42-1
- 1.18.42

* Sun Apr 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.41-1
- 1.18.41

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.40-1
- 1.18.40

* Thu Apr 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.39-1
- 1.18.39

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.38-1
- 1.18.38

* Tue Apr 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.37-1
- 1.18.37

* Mon Apr 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.36-1
- 1.18.36

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.35-1
- 1.18.35

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.34-1
- 1.18.34

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.33-1
- 1.18.33

* Mon Mar 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.32-1
- 1.18.32

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.31-1
- 1.18.31

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.30-1
- 1.18.30

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.29-1
- 1.18.29

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.28-1
- 1.18.28

* Tue Mar 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.27-1
- 1.18.27

* Sat Mar 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.26-1
- 1.18.26

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.25-1
- 1.18.25

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.24-1
- 1.8.24

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.23-1
- 1.8.23

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.22-1
- 1.18.22

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.21-1
- 1.18.21

* Fri Mar 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.20-1
- 1.18.20

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.19-1
- 1.18.19

* Wed Mar 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.18-1
- 1.18.18

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.17-1
- 1.18.17

* Sun Mar 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.16-1
- 1.18.16

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.15-1
- 1.18.15

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.14-1
- 1.18.14

* Wed Mar 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.13-1
- 1.18.13

* Tue Mar 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.12-1
- 1.18.12

* Fri Feb 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.9-1
- 1.18.9

* Thu Feb 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.18.8-1
- Update to 1.18.8

* Fri Feb 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.17.12-1
- Update to 1.17.12

* Wed Jan 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.17.9-1
- Update to 1.17.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.309-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 David Duncan <davdunc@amazon.com> - 1.16.266-1
- Merge changes from 1.16.266 release.

* Mon Oct 21 2019 James Hogarth <james.hogarth@gmail.com> - 1.16.263-2
- Fix changelog syntax
- Remove unused patchfile

* Sat Oct 19 2019 David Duncan <davdunc@amazon.com> - 1.16.263-1
- Merge changes from 1.16.263 release.

* Thu Oct 10 2019 David Duncan <davdunc@amazon.com> - 1.16.253-2
- Merge changes from 1.16.253 release.
- Remove relax-dependencies patch requirement. 

* Fri Oct 04 2019 David Duncan <davdunc@amazon.com> - 1.16.253-1
- Merge changes from 1.16.253 release.

* Thu Oct 03 2019 David Duncan <davdunc@amazon.com> - 1.16.252-1
- Merge changes from 1.16.252 release.

* Thu Oct 03 2019 David Duncan <davdunc@amazon.com> - 1.16.251-1
- Merge changes from 1.16.251 release.

* Tue Oct 01 2019 David Duncan <davdunc@amazon.com> - 1.16.250-1
- Merge changes from 1.16.250 release.

* Mon Sep 30 2019 David Duncan <davdunc@amazon.com> - 1.16.249-1
- Merge changes from 1.16.249 release.

* Sat Sep 28 2019 David Duncan <davdunc@amazon.com> - 1.16.248-1
- Merge changes from 1.16.248 release.

* Thu Sep 26 2019 David Duncan <davdunc@amazon.com> - 1.16.247-1
- Merge changes from 1.16.247 release.

* Wed Sep 25 2019 David Duncan <davdunc@amazon.com> - 1.16.246-1
- Merge changes from 1.16.246 release.

* Sun Sep 22 2019 David Duncan <davdunc@amazon.com> - 1.16.243-1
- Merge changes from 1.16.243 release.

* Thu Sep 19 2019 David Duncan <davdunc@amazon.com - 1.16.241-1
- Update to 1.16.241
 
* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.235-2
- Rebuild with correct patch.

* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.235-1
- Update to 1.16.235.

* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.222-3
- Rebuild for new python-botocore 1.12.225

* Wed Aug 21 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.222-2
- Re-add mistakenly dropped patch.

* Wed Aug 21 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.222-1
- Update to 1.16.222

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.198-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.198-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 David Duncan <davdunc@amazon.com> - 1.16.198-1
- Update to 1.16.198
- Add updates and fixes

* Tue May 28 2019 David Duncan <davdunc@amazon.com> - 1.16.167-1
- Update to 1.16.167
- Add updates and fixes

* Wed Apr 24 2019 David Duncan <davdunc@amazon.com> - 1.16.145-1
- Adding support for ap-east-1 

* Thu Mar 21 2019 David Duncan <davdunc@amazon.com> - 1.16.129-1
- Bumping version to 1.16.129

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.111-1
- Update to 1.16.111

* Mon Feb 11 2019 David Duncan <davdunc@amazon.com> - 1.16.101
- api-change:ecs: Update ecs command to latest version
- api-change:discovery: Update discovery command to latest version
- api-change:dlm: Update dlm command to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.85-2
- Enable python dependency generator

* Mon Nov 19 2018 David Duncan <davdunc@amazon.com> - 1.16.57-1
- Update to 1.16.57. Fixes bug #1613078

* Tue Nov 06 2018 Carl George <carl@george.computer> - 1.16.28-3
- Add patch0 to relax dependencies

* Wed Oct 17 2018 Justin W. Flory <jflory7@fedoraproject.org> - 1.16.28-2
- Add groff dependency, fix 'aws help' issue in stock install

* Sun Oct 07 2018 David Duncan <davdunc@amazon.com> - 1.16.28
- Update to 1.16.28

* Sun Sep 02 2018 David Duncan <davdunc@amazon.com> - 1.15.72-1
- Update to 1.15.72. Updates bug #1613078

* Sun Aug 05 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.71-1
- Update to 1.15.71. Fixes bug #1612393

* Fri Aug 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.70-1
- Update to 1.15.70. Fixes bug #1611853

* Wed Aug 01 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.69-1
- Update to 1.15.69. Fixes bug #1610059

* Fri Jul 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.66-1
- Update to 1.15.66. Fixes bug #1609074

* Thu Jul 26 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.65-1
- Update to 1.15.65. Fixes bug #1608097

* Sun Jul 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.63-1
- Update to 1.15.63. Fixes bug #1606924

* Thu Jul 19 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.62-1
- Update to 1.15.62. Fixes bug #1602972

* Wed Jul 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.60-1
- Update to 1.15.60. Fixes bug #1602176

* Sun Jul 15 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.59-1
- Update to 1.15.59. Fixes bug #1599467

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.53-1
- Update to 1.15.53. Fixes bug #1598936

* Thu Jul 05 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.52-1
- Update to 1.15.52. Fixes bug #1598597

* Wed Jul 04 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.51-2
- Update to 1.15.51. Fixes bug #1596663

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.15.48-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.48-1
- Update to 1.14.48. Fixes bug #1596420

* Thu Jun 28 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.47-1
- Update to 1.14.47. Fixes bug #1595469

* Sat Jun 23 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.45-1
- Update to 1.14.45. Fixes bug #1594465

* Fri Jun 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.44-1
- Update to 1.14.44. Fixes bug #1594038

* Fri Jun 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.43-1
- Update to 1.14.43. Fixes bug #1594038
- Fix python-botocore version to match new python-botocore.

* Wed Jun 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.42-1
- Update to 1.14.42. Fixes bug #1593483

* Wed Jun 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.41-1
- Update to 1.15.41. Fixes bug #1593040

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.15.40-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.40-1
- Update to 1.15.40. Fixes bug #1591986

* Fri Jun 15 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.39-1
- Update to 1.15.39. Fixes bug #1591048

* Tue Jun 12 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.37-1
- Update to 1.15.37. Fixes bug #1590039

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.35-1
- Update to 1.15.35. Fixes bug #1588851

* Wed Jun 06 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.33-1
- Update to 1.15.33. Fixes bug #1586055

* Sun Jun 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.31-1
- Update to 1.15.31. Fixes bug #1583867

* Sun May 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.28-1
- Update to 1.15.28. Fixes bug #1580992

* Fri May 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.24-1
- Update to 1.15.24. Fixes bug #1579995

* Fri May 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.23-1
- Update to 1.15.23. Fixes bug #1579573

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.22-1
- Update to 1.15.22. Fixes bug #1579086

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.21-1
- Update to 1.15.21. Fixes bug #1578162

* Fri May 11 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.19-1
- Update to 1.15.19. Fixes bug #1574745

* Wed May 02 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.12-1
- Update to 1.15.12. Fixes bug #1574052

* Fri Apr 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.10-1
- Update to 1.15.10. Fixes bug #1572396

* Thu Apr 26 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.9-1
- Update to 1.15.9. Fixes bug #1571002

* Mon Apr 23 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.6-1
- Update to 1.15.6. Fixes bug #1570216

* Fri Apr 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.5-1
- Update to 1.15.5. Fixes bug #1569974

* Sat Apr 14 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.4-1
- Update to 1.15.4. Fixes bug #1565379

* Sat Apr 07 2018 Kevin Fenzi <kevin@scrye.com>  - 1.15.2-1
- Update to 1.15.2. Fixes bug #1563195

* Sat Mar 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.68-1
- Update to 1.4.68. Fixes bug #1561240

* Tue Mar 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.64-1
- Update to 1.4.64. Fixes bug #1560762

* Sun Mar 25 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.63-1
- Update to 1.4.63. Fixes bug #1559367

* Fri Mar 23 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.62-1
- Update to 1.4.62. Fixes bug #1559367

* Wed Mar 21 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.60-1
- Update to 1.4.60. Fixes bug #1559193

* Wed Mar 21 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.59-1
- Update to 1.4.59. Fixes bug #1558758

* Sat Mar 17 2018 Kevin Fenzi <kevin@scrye.com>  - 1.14.58-1
- Update to 1.4.58. Fixes bug #1555085

* Tue Mar 13 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.55-1
- Update to 1.4.55. Fixes bug #1555085

* Tue Mar 13 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.54-1
- Update to 1.14.54. Fixes bug #1554552

* Thu Mar 08 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.53-1
- Update to 1.14.53. Fixes bug 1552345

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.50-2
- Update for new python-botocore.

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.50-1
- Update to 1.14.50. Fixes bug #1550746

* Thu Mar 01 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.49-1
- Update to 1.14.49. Fixes bug #1549549

* Sat Feb 24 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.46-1
- Update to 1.14.46. Fixes bug #1546901

* Sat Feb 17 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.41-1
- Update to 1.14.41. Fixes bug #1546437

* Fri Feb 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.40-1
- Update to 1.14.40. Fixes bug #1544045

* Thu Feb 08 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.34-1
- Update to 1.14.34. Fixes bug #1543659

* Wed Feb 07 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.33-1
- Update to 1.14.33. Fixes bug #1542468

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.32-2
- Fix python-botocore version requirement.

* Wed Jan 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.32-1
- Update to 1.14.32. Fixes bug #1481464

* Sun Aug 13 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.133-1
- Update to 1.11.133

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.109-2
- Forgot to update

* Wed Jun 21 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.109-1
- Update to 1.11.109

* Tue May 23 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.90-1
- Update to 1.11.90

* Wed Mar 15 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.63-1
- Update to 1.11.63

* Sat Feb 25 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.55-1
- Update to 1.11.55

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.40-1
- Update to 1.11.40

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.34-2
- Update to 1.11.34

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.11.28-3
- Rebuild for Python 3.6

* Tue Dec 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.28-2
- Add PyYAML dependency

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.28-1
- Update to 1.11.28

* Sat Dec 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.24-1
- Update to 1.11.24

* Thu Nov 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.21-1
- Update to 1.11.21

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.12-1
- Update to 1.11.12

* Sun Oct 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.67-1
- Update to 1.10.67

* Wed Sep 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.62-1
- Update to 1.10.62

* Wed Aug 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.59-1
- Update to current upstream version

* Fri Aug 05 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.53-1
- Update to current upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.45-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.45-1
- Update to current upstream version

* Wed Jun 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.36-1
- Update to current upstream version

* Sat May 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.34-1
- Update to current upstream version

* Wed Feb 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.7-1
- Update to current upstream version

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.6-2
- Fix broken dependency

* Fri Feb 19 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.6-1
- Update to current upstream version

* Wed Feb 17 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.5-1
- Update to current upstream version

* Fri Feb 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.4-1
- Update to current upstream version

* Wed Feb 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.3-1
- Update to current upstream version

* Tue Feb 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.2-1
- Update to current upstream version

* Tue Feb 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.1-1
- Update to current upstream version

* Fri Jan 22 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.0-1
- Update to current upstream version

* Wed Jan 20 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.21-1
- Update to current upstream version
- Don't fix documentation permissions any more (pull request merged)

* Fri Jan 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.920-1
- Update to current upstream version

* Fri Jan 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.19-1
- Update to current upstream version
- Don't substitue the text of bin/aws_bash_completer anymore (pull request merged)
- Don't remove the shabang from awscli/paramfile.py anymore (pull request merged)

* Wed Jan 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.18-1
- Update to current upstream version
- Fix completion for bash
- Remove bcdoc dependency that is not used anymore

* Sun Jan 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.17-1
- Update to current upstream version
- Lock the botocore dependency version

* Sat Jan 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.16-1
- Update to current upstream version
- Add dir /usr/share/zsh
- Add dir /usr/share/zsh/site-functions
- Add MIT license (topictags.py is MIT licensed)
- Move dependency from python-devel to python2-devel
- Add Recommends lines for zsh and bsah-completion for Fedora
- Remove BuildReuires: bash-completion
- Remove the macros py2_build and py2_install to prefer the extended form
- Force non-executable bit for documentation
- Remove shabang from awscli/paramfile.py
- Fix bash completion
- Fix zsh completion
- Remove aws.cmd

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.15-1
- Initial package.
