%bcond_without check

%global goipath         github.com/go-cmd/cmd
Version:                1.0.5

%gometa

%global common_description %{expand:
This package is a small but very useful wrapper around os/exec.Cmd for Linux
and macOS that makes it safe and simple to run external commands in highly
concurrent, asynchronous, real-time applications.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go library wrapper around os/exec.Cmd
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires:  golang(github.com/go-test/deep)
%endif

%description %{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Carl George <carl@george.computer> - 1.0.5-2
- Add github.com/go-test/deep build requirement for tests

* Sat Aug 31 2019 Carl George <carl@george.computer> - 1.0.5-1
- Initial package rhbz#1747622
