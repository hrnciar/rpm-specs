# Do not generate requires for scripts that might not be executed locally.
%global __requires_exclude_from ^%{python3_sitelib}/%{name}/conf

# Some scripts are executed on (non-Fedora) remote host. Do not play with shebangs too much!
%undefine __brp_mangle_shebangs

Name:		cdist
Version:	6.5.5
Release:	3%{?dist}
Summary:	Usable configuration management
License:	GPLv3
URL:		https://www.cdi.st/
Source0:	%pypi_source

BuildArch:	noarch
BuildRequires:	sed
BuildRequires:	findutils
BuildRequires:	grep
BuildRequires:	python3-devel
Requires:	bash
Requires:	openssh-clients

%description
cdist is a usable configuration management system. It adheres to the KISS
principle and is being used in small up to enterprise grade environments. cdist
is an alternative to other configuration management systems.

%prep
%autosetup -p 1 -n %{name}-%{version}

# Remove shebang on non-executable python files.
find . -type f -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python/' {} +

# Assume unverisoned python is python3.
find . -type f -exec sed -i 's/^#!\/usr\/bin\/python$/#!\/usr\/bin\/python3/' {} +

%build
%py3_build

%install
%py3_install

# Restore executable bit on scripts (remove by `python setup.py ...`).
(cd %{buildroot}; grep -l -R -m 1 "^#!\/" . | xargs  chmod +x)

mkdir -p %{buildroot}%{_mandir}/man1/ %{buildroot}%{_mandir}/man7/
cp docs/dist/man/man1/*.1 %{buildroot}%{_mandir}/man1/
cp docs/dist/man/man7/*.7 %{buildroot}%{_mandir}/man7/

%files
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{_mandir}/man7/%{name}-*.7*

%package doc
Summary: Documentation for the cdist configuration management tool

%description doc
HTML documentation for the cdist configuration management tool.

%files doc
%doc docs/dist/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.5.5-3
- Rebuilt for Python 3.9

* Mon May 04 2020 Timothée Floure <fnux@fedoraprojecct.org> - 6.5.5-2
- Remove readme from doc macro (not shipped by upstream anymore).

* Mon May 04 2020 Timothée Floure <fnux@fedoraprojecct.org> - 6.5.5-1
- New upstream release.

* Wed Mar 11 2020 Timothée Floure <fnux@fedoraprojecct.org> - 6.5.2-1
- New upstream release.

* Fri Feb 14 2020 Timothée Floure <fnux@fedoraprojecct.org> - 6.5.0-1
- New upstream release.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Timothée Floure <fnux@fedoraprojecct.org> - 6.4.0-1
- New upstream release.

* Fri Dec 13 2019 Timothée Floure <fnux@fedoraproject.org> - 6.3.0-4
- Disable shebang mangling.

* Fri Dec 13 2019 Timothée Floure <fnux@fedoraproject.org> - 6.3.0-3
- Disable RPM autorequires on cdist types.

* Fri Dec 13 2019 Timothée Floure <fnux@fedoraproject.org> - 6.3.0-2
- Restore script permissions after py3_install macro.
- Cleanup some forgotten python shebangs.

* Thu Dec 12 2019 Timothée Floure <fnux@fedoraprojectc.org> - 6.3.0-1
- New upstream release.

* Sun Dec 01 2019 Timothée Floure <fnux@fedoraprojectc.org> - 6.2.0-1
- Let there be package.
