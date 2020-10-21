%global commit 294f8ee37bb37ab0535558182cf41d99dfb3cb11
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           podman-compose
Version:        0.1.6
Release:        1.git20200615%{?dist}
Summary:        Run docker-compose.yml using podman
License:        GPLv2
URL:            https://github.com/containers/podman-compose
Source0:        https://github.com/containers/podman-compose/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyyaml
Requires:       python3-pyyaml
Requires:       podman

%description
An implementation of docker-compose with podman backend.
The main objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%prep
%autosetup -n %{name}-%{commit}

%build
%py3_build
 
%install
%py3_install 

#Drop spurious shebang
sed -i /python3/d %{buildroot}%{python3_sitelib}/podman_compose.py


%files
%doc README.md CONTRIBUTING.md docs/ examples
%license LICENSE
%{_bindir}/podman-compose
%{python3_sitelib}/__pycache__/podman_compose*pyc
%{python3_sitelib}/podman_compose*

%changelog
* Wed Jul 29 2020 Pavel Raiskup <praiskup@redhat.com> - 0.1.6-1.git20200615
- update to the latest git HEAD; namely to allow spawning privileged containers
  and to fix volume initialization

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5.git20191107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4.git20191107
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3.git20191107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.5-2.git20191107
- Fix for service extension with the same name.

* Mon Oct 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.5-1.git20191030
- Initial build.
