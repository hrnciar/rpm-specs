%global srcname tmuxp

Name:           python-%{srcname}
Version:        1.5.5
Release:        1%{?dist}
Summary:        Tmux session manager

License:        MIT
URL:            https://tmuxp.git-pull.com/
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}
sed -r -i -e 's/([0-9])<([0-9])/\1,<\2/' pyproject.toml requirements/base.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES examples
%{_bindir}/tmuxp
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Mon Aug 24 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.5.5-1
- Update to 1.5.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.1-1
- Initial package
