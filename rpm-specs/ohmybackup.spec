# Generated by go2rpm 1
%bcond_without check

# https://github.com/tismayil/ohmybackup
%global goipath         github.com/tismayil/ohmybackup
%global commit          50f2fcedc1592d34991ccbbb38f7a708e63cabe8

%gometa

%global common_description %{expand:
Scan for backup directories and backup files.}

%global golicenses      LICENSE
%global godocs          README.md files/files.txt files/folders.txt\\\
                        files/extensions.txt

Name:           ohmybackup
Version:        0
Release:        0.2%{?dist}
Summary:        Scan for backup directories and backup files

License:        GPLv2
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/ohmybackup %{goipath}

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
%doc README.md files/files.txt files/folders.txt files/extensions.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200405git50f2fce
- Initial package

