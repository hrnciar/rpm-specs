# Generated by go2rpm 1
%bcond_without check

# https://github.com/tomnomnom/meg
%global goipath         github.com/tomnomnom/meg
Version:                0.2.4

%gometa

%global common_description %{expand:
Fetch many paths for many hosts without killing the hosts.}

%global golicenses      LICENSE
%global godocs          README.mkd

Name:           meg
Release:        1%{?dist}
Summary:        Fetch many paths for many hosts

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/tomnomnom/rawhttp)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/meg %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.mkd
%{_bindir}/*

%gopkgfiles

%changelog
* Sat May 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.4-1
- Initial package
