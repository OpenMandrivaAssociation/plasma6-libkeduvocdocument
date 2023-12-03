%define major 5
%define libname %mklibname KEduVocDocument
%define devname %mklibname KEduVocDocument -d

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Free Educational Software based on the KDE technologies
Name:		plasma6-libkeduvocdocument
Version:	24.01.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkeduvocdocument-%{version}.tar.xz
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
Requires:	%{libname} = %{EVRD}

%description
Runtime library for KDE Education Application.

%files -f libkeduvocdocument.lang

#---------------------------------------------

%package -n %{libname}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Runtime library for KDE Education Application

%files -n %{libname}
%{_libdir}/libKEduVocDocument.so.%{major}*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description  -n %{devname}
Files needed to build applications based on %{name}.

%files  -n %{devname}
%{_includedir}/libkeduvocdocument
%{_libdir}/libKEduVocDocument.so
%{_libdir}/cmake/libkeduvocdocument

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n libkeduvocdocument-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkeduvocdocument
