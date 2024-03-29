# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

Summary:	Python interface to systemd
Name:		python-systemd
Version:	235
Release:	1
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/systemd/python-systemd
Source0:	https://github.com/systemd/python-systemd/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libsystemd)

%description
Provides Python scripting interface to systemd.

%prep
%autosetup -p1

%build
%if %{cross_compiling}
export PKG_CONFIG_PATH="%{_prefix}/%{_target_platform}/%{_lib}/pkgconfig"
%endif
%make_build PYTHON=%{__python} CC="%{__cc}"

%install
%if %{cross_compiling}
export PKG_CONFIG_PATH="%{_prefix}/%{_target_platform}/%{_lib}/pkgconfig"
%endif
%make_install PYTHON=%{__python} CC="%{__cc}"

%files
%doc README.md LICENSE.txt NEWS
%dir %{py_platsitedir}/systemd
%{py_platsitedir}/systemd/test/*.py
%{py_platsitedir}/systemd/*.py
%{py_platsitedir}/systemd/*.so
%{py_platsitedir}/*.egg-info
