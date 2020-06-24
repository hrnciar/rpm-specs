Name:           ilua
Version:        0.2.1
Release:        1%{?dist}
Summary:        Portable Lua kernel for Jupyter

License:        GPLv2
URL:            https://github.com/guysv/ilua

# This source contains the Lua logo
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/UDFBEBDR4NTSP6TATQEONDJAYHSYXUUQ/
# Source0:      %%{url}/archive/%%{version}/%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}-nologo.tar.gz
# Use this script (version as first argument) to generate the above tarball
Source1:        create-nologo-source.sh

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
%{_datadir}/jupyter/kernels/lua/

%changelog
* Mon May 11 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-1
- Initial package (#1834280)
