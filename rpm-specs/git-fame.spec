Name:           git-fame
Version:        1.12.0
Release:        2%{?dist}
Summary:        Pretty-print git repository collaborators sorted by contributions

License:        MPLv2.0
URL:            https://pypi.python.org/pypi/git-fame
Source0:        %{pypi_source}

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       git-core
Requires:       python%{python3_version}dist(argopt) >= 0.3.5
# Only for beautifulness
Recommends:     python%{python3_version}dist(tqdm)
Recommends:     python%{python3_version}dist(tabulate)

%description
Pretty-print git repository collaborators sorted by contributions.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_libexecdir}/git-core
ln -s %{_bindir}/%{name} %{buildroot}%{_libexecdir}/git-core/%{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 gitfame/git-fame.1

%check
# Tests depend on real git repo

%files
%license LICENCE
%doc README.rst
%{_bindir}/%{name}
%{_libexecdir}/git-core/%{name}
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/git_fame-*.egg-info/
%{python3_sitelib}/gitfame/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Mon Sep 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-2
- Add missing Requires

* Sun Sep 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Wed Dec 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.1.0-1
- Initial package.
