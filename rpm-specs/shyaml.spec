Name:           shyaml
Version:        0.6.1
Release:        8%{?dist}
Summary:        YAML for command line

License:        BSD
URL:            https://github.com/0k/shyaml
Source0:        https://github.com/0k/shyaml/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Avoids the need to run autogen.sh during setup (which requires the complete
# git repository). Recreate by running './autogen.sh' in a local git checkout
Patch0:         %{name}.autogen.patch
# Remove CHANGELOG from the files to install, as it does not exist.
Patch1:         %{name}.filelist.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist d2to1}
BuildRequires:  %{py3_dist pyyaml}

%description
Simple scripts that allow read access to YAML files through command line.  This
can be handy, if you want to get access to YAML data in your shell scripts.
This scripts supports only read access and it might not support all the
subtleties of YAML specification. But it should support some handy basic query
of YAML file.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/shyaml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.6.1-7
- Explicitly BR python3-setuptools (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Remove check section, no tests were run

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.5.0-3
- Remove unnecessary shebang replacement (done by the installer)

* Fri Dec 29 2017 Till Hofmann <thofmann@fedoraproject.org> - 0.5.0-2
- Remove CHANGELOG from the installed files (CHANGELOG does not exist)

* Thu Apr 27 2017 Till Hofmann <thofmann@fedoraproject.org> - 0.5.0-1
- Initial package
