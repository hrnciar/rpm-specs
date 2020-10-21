# Generated by go2rpm 1
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/istio/viper
%global goipath         github.com/istio/viper
Version:                1.3.2
%global commit 8c945bc35dc260588278ff26d25042b30ae6952e

%gometa

%global common_description %{expand:
Go configuration with fangs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go configuration with fangs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/spf13/viper/issues/947
Patch0:         0001-Remove-TestBindPFlagsStringSlice.patch

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
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(github.com/xordataexchange/crypt/config)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Aug 11 22:06:40 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.2-1.20200811git8c945bc
- Initial package
