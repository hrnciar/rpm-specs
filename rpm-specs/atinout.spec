Name:           atinout
Summary:        AT commands as input are sent to modem and responses given as output
Version:        0.9.1
Release:        1%{?dist}
License:        GPLv3+

URL:            https://atinout.sourceforge.net/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}-%{version}.tar.gz

# Remove the custom build flags that override fedora build flags, continue to append -DVERSION for build to succeed 
Patch0:        0001-remove-custom-flags.patch

BuildRequires:  gcc

%global _hardened_build 1

%description
This program will read a file (or stdin) containing a list of AT
commands. Each command will be send to the modem, and all the response
for the command will be output to file (or stdout).

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install

%files
%{_bindir}/atinout
%{_mandir}/man1/atinout.1*
%doc README atinout.1.html logo/atinout.svg
%license gplv3.txt

%changelog
* Wed Aug 26 2020 Torrey Sorensen <sorensentor@tuta.io> - 0.9.1-1
- initial packaging
