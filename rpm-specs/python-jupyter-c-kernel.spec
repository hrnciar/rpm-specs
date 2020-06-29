%global srcname jupyter-c-kernel
%global srcname_ jupyter_c_kernel

Name:           python-%{srcname}
Version:        1.2.2
Release:        9%{?dist}
Summary:        Minimalistic C kernel for Jupyter

License:        MIT
URL:            https://github.com/brendanrius/jupyter-c-kernel
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname_}/%{srcname_}-%{version}.tar.gz
# https://github.com/brendan-rius/jupyter-c-kernel/pull/46
Source1:        README.md
Source2:        LICENSE.txt
# https://github.com/brendan-rius/jupyter-c-kernel/pull/47
Patch0001:      0001-Use-tempfile-instead-of-IPython-to-get-a-temp-dir.patch
 
BuildArch:      noarch

%global _description \
%{summary}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jupyter-client

Requires:       gcc
Requires:       python3-jupyter-client
Requires:       python3-ipykernel

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname_}-%{version} -p1
cp -p %SOURCE1 %SOURCE2 .

# Remove bundled egg-info
rm -rf %{srcname_}.egg-info


%build
%py3_build


%install
%py3_install

%{__python3} %{buildroot}%{_bindir}/install_c_kernel --prefix %{buildroot}%{_prefix}
rm %{buildroot}%{_bindir}/install_c_kernel


%files -n python3-%{srcname}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{srcname_}-%{version}-py%{python3_version}.egg-info
%{_datadir}/jupyter/kernels/c


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Initial package.
