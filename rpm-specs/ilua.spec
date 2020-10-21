Name:           ilua
Version:        0.2.1
Release:        3%{?dist}
Summary:        Portable Lua kernel for Jupyter

# The package contains the Lua logo, which has some modification restrictions.
# It was permitted by legal, but advised not to declare the license in the tag:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/UDFBEBDR4NTSP6TATQEONDJAYHSYXUUQ/
# Hence, only listing the license of the code.
License:        GPLv2
URL:            https://github.com/guysv/ilua
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

Requires:       python-jupyter-filesystem
Recommends:     lua

%description
ILua is a feature-packed, portable console and Jupyter kernel for the Lua
language. It is Lua-implementation agnostic, should work with any Lua
interpreter out of the box.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ilua

%files -f %pyproject_files
%license LICENSE
%doc README.md CHANGES.md
%{_bindir}/ilua
%dir %{_datadir}/jupyter/kernels/lua/
%{_datadir}/jupyter/kernels/lua/*.json
%{_datadir}/jupyter/kernels/lua/*.png
%license %{_datadir}/jupyter/kernels/lua/logo-license.txt

%changelog
* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Include the Lua logo from upstream

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-1
- Initial package (#1834280)
