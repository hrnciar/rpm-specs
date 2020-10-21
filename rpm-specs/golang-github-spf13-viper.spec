# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/spf13/viper
%global goipath         github.com/spf13/viper
Version:                1.7.1

%gometa

%global goipaths0       github.com/spf13/viper
%global goipathsex0     github.com/spf13/viper/remote

%if %{without bootstrap}
%global goipaths1       github.com/spf13/viper/remote
%endif

%global common_description %{expand:
Viper is a complete configuration solution for Go applications including
12-Factor apps. It is designed to work within an application, and can handle all
types of configuration needs and formats. It supports:

 - setting defaults
 - reading from JSON, TOML, YAML, HCL, and Java properties config files
 - live watching and re-reading of config files (optional)
 - reading from environment variables
 - reading from remote config systems (etcd or Consul), and watching changes
 - reading from command line flags
 - reading from buffer
 - setting explicit values

Viper can be thought of as a registry for all of your applications configuration
needs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go configuration with fangs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/spf13/viper/issues/947
Patch0:         0001-Remove-TestBindPFlagsStringSlice-and-TestBindPFlagsIntSlice.patch

%if %{without bootstrap}
BuildRequires:  golang(github.com/bketelsen/crypt/config)
%endif
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/printer)
BuildRequires:  golang(github.com/magiconair/properties)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/spf13/cast)
BuildRequires:  golang(github.com/spf13/jwalterweatherman)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/subosito/gotenv)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%if %{with bootstrap}
%gocheck -d remote
%else
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Sun Aug 02 21:32:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.2-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 23:21:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1
- Release 1.4.0

* Tue Apr 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0.0-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-2.git25b30aa
- Update to spec 3.0

* Wed Feb 21 2018 Kaushal <kshlmster@gmail.com> - 1.0.0-1
- Update to upstream v1.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitc1de958
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitc1de958
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitc1de958
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gitc1de958
- Bump to upstream c1de95864d73a5465492829d7cb2dd422b19ac96
  related: #1414254

* Mon Mar 06 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git1699063
- Use the default weather import path prefix
  related: #1414254

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git1699063
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git1699063
- Bump to upstream 16990631d4aa7e38f73dbbbf37fa13e67c648531
  resolves: #1414254

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitbe5ff3e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitbe5ff3e
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitbe5ff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbe5ff3e
- First package for Fedora
  resolves: #1270064
