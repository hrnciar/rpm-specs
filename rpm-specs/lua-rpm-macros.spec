%if 0%{?el8}
# RHEL's lua-devel ships macros.lua and lua.attr
# skip shipping lua-rpm-macros so we don't conflict
%bcond_with rpm_macros
%else
%bcond_without rpm_macros
%endif

%if 0%{?fedora} >= 33
# requires RPM >= 4.16
%bcond_without requires_generator
%else
%bcond_with requires_generator
%endif

Name:           lua-rpm-macros
Version:        1
Release:        2%{?dist}
Summary:        The common Lua RPM macros

License:        MIT

# Macros:
Source101:      macros.lua
Source102:      macros.lua-srpm       

# RPM requires generator
Source103:      lua.attr

# license text
Source200:      LICENSE

BuildArch:      noarch

# for lua_libdir and lua_pkgdir
Requires:       lua-srpm-macros = %{version}-%{release}

%description
This package contains Lua RPM macros.

You should not need to install this package manually as lua-devel requires it.


%package -n lua-srpm-macros
Summary:        RPM macros for building Lua source packages

# For directory structure
Requires:       redhat-rpm-config

%description -n lua-srpm-macros
RPM macros for building Lua source packages.


%prep
%autosetup -c -T
cp -a %{sources} .
%if %{without rpm_macros}
rm macros.lua
%endif


%build


%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -pm 644 macros.* %{buildroot}%{rpmmacrodir}/
%if %{with requires_generator}
install -Dpm 0644 lua.attr %{buildroot}/%{_fileattrsdir}/lua.attr
%endif


%if %{with rpm_macros}
%files
%license LICENSE
%if %{with requires_generator}
%{_fileattrsdir}/lua.attr
%endif
%{rpmmacrodir}/macros.lua
%endif

%files -n lua-srpm-macros
%license LICENSE
%{rpmmacrodir}/macros.lua-srpm


%changelog
* Mon Aug 31 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1-2
- Also move lua.attr requires generator

* Fri Aug 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1-1
- Initial package
